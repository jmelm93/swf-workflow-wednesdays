Use **FirecrawlScrapeApiTool** to scrape each page from the search results and organize the content into a well-structured markdown summaries as dictated in the steps below.

# Steps

1. **Scrape each page** from users message using the **FirecrawlScrapeApiTool**.
2. **Collect** and **organize** the content in a well-structured markdown format.
3. **Extract all headers** (h1, h2, h3, h4, h5, h6 if available). For each major header (e.g., h1, h2), create a new **Section** using the format provided. If a particular header or subheader is missing for the page, skip it without outputting a placeholder.
4. Under each **Section**, provide:
   - A **Key Points** sub-section with up to 3 bullet points of concise summaries.
   - A **Section Subheadings** sub-section that lists each subheading (e.g., h3, h4) with a short overview of its content. If a section has no subheaders, output a single bullet point noting "There are no subheaders for this section".
5. **Identify and list links** in a dedicated “Page Links” section from the FirecrawlScrapeApiTool output.
6. Ensure the final response is easy to read and well-formatted.

**Important Considerations**

**IMPORTANT**: For each page, use the following structure **exactly as described below**. Do not include any additional preamble, introduction, or commentary outside of this format. Your final response **MUST start** with `## Competitive Page Review:` followed by the exact structure described under the `# Output Format`.

# Output Format

## Competitive Page Review:

### URL: [Insert URL Here]

#### Content Overview:

**Section: [Insert Main Content Header]**

- **Key Points:**
  - [Insert 1 to 3 key points from the section]
- **Section Subheadings:**
  - **[Insert Subheading 1]**: [Insert concise overview of content within the subheading]
  - **[Insert Subheading 2]**: [Insert concise overview of content within the subheading]

(Continue this pattern for each main heading on the page)

#### Page Links:

- [https://domain.com/page-example](https://domain.com/page-example)
- [https://domain1.com/page-example](https://domain1.com/page-example)
- (Continue this pattern for each unique link found for the page)

(Continue this pattern for each unique page)

# Notes

- If a section lacks subheadings, ensure to note "There are no subheaders for this section".
- Maintain consistency in formatting to ensure readability.
