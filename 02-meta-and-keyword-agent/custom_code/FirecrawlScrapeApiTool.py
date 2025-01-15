from langflow.custom import Component
from pydantic import BaseModel, Field
from langchain_core.tools import ToolException
from langchain.tools import StructuredTool
from langflow.base.langchain_utilities.model import LCToolComponent
from langflow.field_typing import Tool
from langflow.io import (
    DataInput,
    IntInput,
    SecretStrInput,
    StrInput,
)
from langflow.schema import Data


class FirecrawlScrapeApiSchema(BaseModel):
    url: str = Field(..., description="The URL to scrape.")


class FirecrawlScrapeApiTool(LCToolComponent):
    display_name: str = "FirecrawlScrapeApiTool"
    description: str = "Firecrawl Scrape API (Tool)."
    name = "FirecrawlScrapeApiTool"

    output_types: list[str] = ["Document"]
    documentation: str = "https://docs.firecrawl.dev/api-reference/endpoint/scrape"

    inputs = [
        SecretStrInput(
            name="api_key",
            display_name="API Key",
            required=True,
            password=True,
            info="The API key to use Firecrawl API.",
        ),
        StrInput(
            name="url",
            display_name="URL",
            # required=True,
            info="The URL to scrape.",
        ),
        IntInput(
            name="timeout",
            display_name="Timeout",
            info="Timeout in milliseconds for the request.",
        ),
        DataInput(
            name="scrapeOptions",
            display_name="Scrape Options",
            info="The page options to send with the request.",
        ),
        DataInput(  # https://docs.firecrawl.dev/features/extract
            name="extractorOptions",
            display_name="Extractor Options",
            info="The extractor options to send with the request.",
        ),
    ]

    def build_tool(self) -> Tool:
        """Build the tool for use in agents."""
        return StructuredTool.from_function(
            name="FirecrawlScrapeApiTool",
            description="Firecrawl Scrape API (Tool).",
            func=self._scrape,
            args_schema=FirecrawlScrapeApiSchema,
        )


    def _scrape(self, url: str) -> list[Data]:
        try:
            from firecrawl.firecrawl import FirecrawlApp
        except ImportError as e:
            msg = "Could not import firecrawl integration package. Please install it with `pip install firecrawl-py`."
            raise ImportError(msg) from e

        try:
            params = self.scrapeOptions.__dict__["data"] if self.scrapeOptions else {}
            extractor_options_dict = self.extractorOptions.__dict__["data"] if self.extractorOptions else {}
            if extractor_options_dict:
                params["extract"] = extractor_options_dict

            app = FirecrawlApp(api_key=self.api_key)
            results = app.scrape_url(url, params=params)
            return Data(data=results)

        except Exception as e:
            raise ToolException(f"Error while scraping URL: {e}") from e