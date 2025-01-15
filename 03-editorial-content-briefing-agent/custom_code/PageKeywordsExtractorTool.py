from typing import Dict, Any, List, Optional
from http.client import HTTPSConnection
from base64 import b64encode
from json import loads
from json import dumps
from typing import Dict, Any
from pydantic import Field, BaseModel
from langchain.tools import StructuredTool
from langflow.base.langchain_utilities.model import LCToolComponent
from langflow.field_typing import Tool
from langflow.inputs import SecretStrInput, MessageTextInput
from langflow.schema import Data


class DataForSEOJobInputs(BaseModel):
    endpoint: str = Field(description="DataForSEO endpoint")
    params: Dict[str, Any] = Field(description="DataForSEO job parameters")


class DataForSEOJobRunner:
    def __init__(self, username: str, password: str):
        self.client = DataForSEOClient(username, password)
        
    def run(self, job_inputs: DataForSEOJobInputs):
        response = self.client.post(job_inputs.endpoint, {"data": job_inputs.params})
        if response["status_code"] == 20000:
            return response
        else:
            raise Exception(f"API request failed with status code {response['status_code']} and message: {response['status_message']}")


class DataForSEOClient:
    domain = "api.dataforseo.com"

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def request(self, path, method, data=None):
        connection = HTTPSConnection(self.domain)
        try:
            base64_bytes = b64encode(
                ("%s:%s" % (self.username, self.password)).encode("ascii")
                ).decode("ascii")
            headers = {'Authorization' : 'Basic %s' %  base64_bytes, 'Content-Encoding' : 'gzip'}
            connection.request(method, path, headers=headers, body=data)
            response = connection.getresponse()
            return loads(response.read().decode())
        finally:
            connection.close()

    def get(self, path):
        return self.request(path, 'GET')

    def post(self, path, data):
        if isinstance(data, str):
            data_str = data
        else:
            data_str = dumps(data)
        return self.request(path, 'POST', data_str)

    
class PageKeywordsExtractorToolSchema(BaseModel):
    url: str = Field(..., description="The URL to scrape.")


class PageKeywordsExtractorTool(LCToolComponent):
    display_name: str = "PageKeywordsExtractorTool"
    description: str = "Gets keywords for a page using DataForSEO API"
    name = "PageKeywordsExtractorTool"

    inputs = [
        MessageTextInput(
            name="dataforseo_username",
            display_name="DataForSEO Username",
            required=True,
            info="The username to use the DataForSEO API.",
        ),
        SecretStrInput(
            name="dataforseo_password",
            display_name="DataForSEO Password",
            required=True,
            info="The password to use the DataForSEO API.",
        ),
        MessageTextInput(
            name="url",
            display_name="URL",
            info="The URL to scrape.",
        ),
    ]

    def build_tool(self) -> Tool:
        """Build the tool for use in agents."""
        return StructuredTool.from_function(
            name="dataforseo_page_keywords_extractor",
            description="Get keywords for a page using DataForSEO API.",
            func=self._run,
            args_schema=PageKeywordsExtractorToolSchema,
        )

    def _create_post_data(self, page_target: str) -> dict:
        """
        Creates the POST data for the API call with filters, ordering, and limits for a single URL.

        Returns:
            dict: Dictionary formatted for the API call.
        """
        filters = [
            ["keyword_data.keyword_info.search_volume", ">", 10],
            "and",
            ["ranked_serp_element.serp_item.type", "=", "organic"],
        ]

        order_by = [
            "ranked_serp_element.serp_item.etv,desc",
            "ranked_serp_element.serp_item.rank_absolute,asc"
        ]

        return {
            "target": page_target,
            "location_name": "United States",
            "language_name": "English",
            "filters": filters,
            "order_by": order_by,
            "limit": 5
        }

    def _extract_keywords_data(self, data) -> str:
        """
        Extracts and formats keyword data from the API response.

        Returns:
            str: Formatted string of keywords and their search volumes.
        """
        keyword_strings = []
        tasks = data.get("tasks", [])
        
        for task in tasks:
            task_results = task.get("result", [])
            
            if task_results:
                for res in task_results:
                    items = res.get("items", [])
                    
                    if items:
                        for item in items:
                            keyword_data = item.get("keyword_data", {})
                            search_volume = keyword_data.get("keyword_info", {}).get("search_volume")
                            keyword = keyword_data.get("keyword")
                            
                            # Append to result list if all required fields are present
                            if keyword and search_volume:
                                keyword_strings.append(f"{keyword} ({search_volume} searches/mo)")
            
        return ', '.join(keyword_strings)

    def _run(self, url: str) -> list[Data]:
        """
        Runs the job for each URL in page_targets and returns a formatted string with URL and keyword data.

        Returns:
            str: Formatted string with each URL and its associated keywords and search volumes.
        """

        job_runner = DataForSEOJobRunner(self.dataforseo_username, self.dataforseo_password)
        params = self._create_post_data(url)
        job_inputs = DataForSEOJobInputs(
            endpoint="/v3/dataforseo_labs/google/ranked_keywords/live",
            params=params
        )

        response = job_runner.run(job_inputs)
        if response["status_code"] == 20000:
            # return self._extract_keywords_data(response)
            returned_data = self._extract_keywords_data(response)
            return [
                Data(text_key="keywords", data={"keywords": returned_data, "url": url})
            ]
        else:
  
            return [
                Data(text_key="error", data={"error": f"DataforSeo API Error: {response['status_message']}", "url": url})
            ]
    