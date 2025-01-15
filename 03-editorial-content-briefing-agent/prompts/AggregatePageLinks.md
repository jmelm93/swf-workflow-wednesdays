You will be provided with content outlines and lists of links from multiple pages. Your task is to consolidate the links from across these outputs.

# Steps

1. Identify the "Page Links" section in the provided outputs.
2. Extract all links listed under "Page Links" for each page.
3. Remove duplicate links to create a consolidated list of unique links.
4. For each unique link, list **all the pages** (by their respective page URLs) where the link was found.

**IMPORTANT**: Do not include any additional preamble, commentary, or formatting outside of this structure. The start of your response MUST be "## Consolidated Links:".

# Output Format

- Start with "## Consolidated Links:".
- Present the data as a markdown table with two columns: "Link" and "Found on".
- Format each link as [https://domain.com](https://domain.com).
- In the "Found on" column, list all page URLs where the link was found, separated by commas, each formatted as [https://linkingpage.com/page](https://linkingpage.com/page).
- Do not use code blocks.

# Examples

## Consolidated Links:

| Link                                       | Found on                                                                                                                       |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| [https://domain1.com](https://domain1.com) | [https://linkingpage1.com/page](https://linkingpage1.com/page), [https://linkingpage2.com/page](https://linkingpage2.com/page) |
| [https://domain2.com](https://domain2.com) | [https://linkingpage1.com/page](https://linkingpage1.com/page)                                                                 |
