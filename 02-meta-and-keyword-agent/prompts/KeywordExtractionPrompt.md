# Search Results

{serp_data}

# Instructions

Use the **PageKeywordsExtractorTool** to extract keywords for each provided URL and compile the results into a markdown table.

Follow these steps:

1. **Extract keywords** for each URL using PageKeywordsExtractorTool.
2. **Organize** the extracted keywords and corresponding URLs into a markdown table.

**Important:** Ensure that your response starts with "## Competitive Keyword Targets:" and follows the exact structure as described below. Do not include any additional preamble, introduction, or commentary outside of this format.

# Output Format

Your response must begin with:

## Competitive Keyword Targets:

Followed by a markdown table with two columns: "URL" and "Keywords". Each row should list the URL and its associated keywords, including search volumes in the following format:

| URL    | Keywords                                                    |
| ------ | ----------------------------------------------------------- |
| [URL1] | [keyword1] (X searches/mo), [keyword2] (Y searches/mo), ... |
| [URL2] | [keyword1] (X searches/mo), [keyword2] (Y searches/mo), ... |

[Continue for all URLs provided...]

# Examples

**Example input:**

# Search Results

https://example.com  
https://anotherexample.com

**Example output:**

## Competitive Keyword Targets:

| URL                        | Keywords                                                 |
| -------------------------- | -------------------------------------------------------- |
| https://example.com        | apples (120 searches/mo), bananas (95 searches/mo), ...  |
| https://anotherexample.com | cameras (500 searches/mo), lenses (300 searches/mo), ... |

[Continue for all URLs provided...]
