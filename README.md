
# UX Analyser

This project, UX Analyzer, is a tool built with Python to evaluate and improve how user-friendly a website is. It analyzes different parts of a webpage, like its structure, accessibility, and design, to give useful feedback on how well the website follows good UX practices.

The tool checks things like whether headings are organized correctly, if images have descriptive text (alt text), and if there are any broken links. It also looks at how readable the text is, whether the site is mobile-friendly, and if it loads quickly. For modern websites that use JavaScript to load content, the tool uses Selenium to handle and analyze those pages too.

After the analysis, the tool creates a report with a score for the website's user experience and detailed suggestions to improve specific areas. This makes it easy for developers, designers, and businesses to understand what’s working well and what needs improvement.

In short, this project helps websites become more user-friendly, accessible, and effective in delivering a great experience to visitors.

## Features

- **Proper Heading Structure:** Ensures the webpage has a logical and hierarchical structure of headings (<h1> to <h6>).
- **Mobile Responsiveness:** Checks if the webpage includes a viewport meta tag, indicating mobile-friendly design.
- **Text Readability:** Evaluates the presence of readable text (e.g., paragraphs) on the webpage.
- **Alt Text for Images:** Verifies that all images include descriptive alt text for accessibility.
- **Presence of Call-to-Action (CTA):** Identifies buttons and links with action-oriented text to ensure clear CTAs are available.
- **No Broken Links:** Analyzes links on the webpage and flags any that are broken or inaccessible.
- **Page Load Speed:** Measures the time taken to load the webpage, ensuring it is optimized for user satisfaction.
- **Accessibility for Screen Readers:** Checks for ARIA labels and semantic landmarks (<nav>, <header>, etc.) to support screen readers.
- **Favicon Presence:** Confirms the presence of a favicon for a polished and professional appearance.
- **Visual Report Generation:** Creates a bar chart visualization of the UX analysis results and saves it as an image.
## Tech Stack

**Programming Language:** Python

**Libraries:**
- BeautifulSoup: Parses HTML content to analyze elements like headings, images, and links.
- Requests: Handles HTTP requests to fetch webpage data for analysis.
- URllib: Assists in parsing URLs to manage relative and absolute link structures.
- Matplotlib: Generates visual representations of the UX analysis results, such as bar charts.


## Usage

- Enter the URL of the webpage to analyze in the input form.
- (Optional) Provide additional settings or custom rules.
- Click "Analyze" to start the process.
- View the results, including scores for individual rules and overall UX effectiveness.


## Demo




## Future Improvements

- Support for multilingual websites.
- Advanced scoring metrics for usability and aesthetics.
- Integration with analytics tools for deeper insights.
