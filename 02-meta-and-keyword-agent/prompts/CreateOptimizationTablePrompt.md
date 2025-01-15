Create a markdown table with SEO-optimized and compelling metadata for articles.

# Steps

1. **Populate Target Page Column**: Use the provided `<target_page_and_topic>` to identify the target page for each row in the table.
2. **Populate Keyword Targets Column**: Take the keywords provided in `<keyword_targets>`, remove duplicates, and remove any keywords that are semantically unrelated to the main topic of the target page or have demonstrably different search intent based on the `<current_page_content>`. Order the remaining keywords by their search volume in descending order, starting with the highest. Format each keyword in the final list with its search volume as provided (e.g., Keyword Target (Search Volume)).
3. **Provide Reasoning**: Explain the rationale behind your choices for the Title Tag and Description.
4. **Create Title Tag**: Develop an SEO-optimized and compelling title tag for the target page. Apply the `<title>` tag best practices outlined below when creating the title tag. **When including a subtitle or secondary information, use either brackets `[]` or parentheses `()` to separate it from the main title.**
5. **Create Meta Description**: Write a concise and engaging meta description for the target page that accurately summarizes the content and encourages clicks. Incorporate relevant keywords naturally. Keep the description within a maximum of 170 characters.

When optimizing the `<title>` tag, use the best practices below:

1. **Include Primary Keywords:** Ensure the main keywords for the page are present in the title tag.
2. **Use Structured Syntax:** Organize titles with clear structures, incorporating elements like brackets, parentheses, or separators (e.g., `|` or `–`) to improve clarity and click-through rates. **Prioritize brackets `[]` or parentheses `()` for separating main title from subtitle.**
3. **Keep Length Balanced:** Avoid overly long or short titles. Ensure titles include necessary keywords without redundancy.
4. **Incorporate Relevant Variations:** Use additional keyword variations if they align with the same search intent, but avoid unnecessary repetition.
5. **Enhance Readability for CTR:** Utilize formatting elements like brackets and parentheses to make titles more engaging without overloading with symbols or keywords.
6. **Match Context to Content Type:** Adapt title structure to the page’s purpose, such as commercial or editorial, for relevance and user appeal.

# Output Format

Provide a markdown table with the following columns: **Target Page**, **Keyword Targets**, **Title Tag**, **Description**, and **Reasoning**. Ensure the "Keyword Targets" column lists the highest quality keyword targets for the target page, formatted with their search volumes (e.g., Keyword Target (Search Volume)). Do not use code blocks.

# Examples

| Target Page                                | Keyword Targets                                                                                                      | Title Tag                                             | Description                                                                                                             | Reasoning                                                                                                                                                                                                               |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| https://www.example.com/best-running-shoes | running shoes (210,000 searches/mo), best running shoes (10,000 searches/mo), good running shoes (8,000 searches/mo) | Best Running Shoes 2025 (Top Sneaker Picks & Reviews) | Find the best running shoes for your needs in 2025! Expert reviews and top picks for comfort and performance.           | Used "best running shoes" (high volume) naturally as the primary keyword. Parentheses were used to enhance readability and CTR.                                                                                         |
| https://www.example.com/trail-running-gear | trail running gear (50,000 searches/mo), best trail shoes (40,000 searches/mo)                                       | Top Trail Running Gear 2025 [Shoes, Backpacks & More] | Explore essential trail running gear for 2025. Expert reviews on shoes, backpacks, and apparel for your next adventure. | Focused on the highest volume keyword "trail running gear." The title uses brackets for structure. "Trail running backpack" was considered less central to the overall page and therefore not prioritized in the title. |
