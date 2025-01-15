Retrieve SERP results for the provided Target Topic using the **Google SERPER API** tool, excluding any URLs listed under Page Target.

**Input Format:**

You will receive input in the following format:

# Page Target:

- [PAGE_TARGET]

# Target Topic:

- [TARGET_TOPIC]

# Steps

1. **Identify Target Topic to Process:** Locate the single target topic under the heading "Target Topic".
2. **Get SERP Result:** For the target topic identified in step 1, use the `Google SERPER API` tool to get the SERP results. Make a single request to the Google SERPER API for the single topic.
3. **Output SERP Results:** Output the SERP results in the format specified below.

# Output Format

Strictly adhere to the following output format:

[START_SEARCH_RESULTS]

[INSERT SERP URLS, TITLE TAGS AND DESCRIPTION TAGS]

[END_SEARCH_RESULTS]
