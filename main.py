import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# Predefined UX rules (this is a basic example, more detailed rules can be added)
UX_RULES = {
    "1. Proper Heading Structure": lambda soup: check_headings_structure(soup),
    "2. Mobile Responsiveness": lambda url: check_mobile_responsiveness(url),
    "3. Text Readability (Contrast and Font Size)": lambda soup: check_text_readability(soup),
    "4. Alt Text for Images": lambda soup: check_image_alt_text(soup),
    "5. Presence of Call to Action (CTA)": lambda soup: check_cta_buttons(soup),
}

# Function to scrape the webpage
def scrape_webpage(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    except Exception as e:
        print(f"Error accessing the URL: {e}")
        return None

# UX Check 1: Proper heading structure (H1, H2, etc.)
def check_headings_structure(soup):
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    return len(headings) > 0  # You can add more complex checks here (like checking order)

# UX Check 2: Mobile Responsiveness
def check_mobile_responsiveness(url):
    # Check if viewport meta tag is present
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    viewport = soup.find('meta', {'name': 'viewport'})
    return viewport is not None

# UX Check 3: Text Readability (Contrast, Font size) - Dummy check here
def check_text_readability(soup):
    # More complex analysis using CSS might be necessary; just checking for paragraphs here
    paragraphs = soup.find_all('p')
    return len(paragraphs) > 0

# UX Check 4: Alt text for images
def check_image_alt_text(soup):
    images = soup.find_all('img')
    missing_alt = [img for img in images if not img.get('alt')]
    return len(missing_alt) == 0

# UX Check 5: Presence of Call to Action (CTA) buttons
def check_cta_buttons(soup):
    buttons = soup.find_all('button') + soup.find_all('a', href=True)
    # Check if any button or anchor has a CTA-like word
    cta_words = ['buy', 'subscribe', 'learn more', 'contact', 'sign up']
    for btn in buttons:
        if any(word in btn.text.lower() for word in cta_words):
            return True
    return False

# Main function to analyze the webpage based on the UX rules
def analyze_webpage(url):
    soup = scrape_webpage(url)
    if not soup:
        return

    results = {}
    for rule, check_function in UX_RULES.items():
        result = check_function(soup) if 'soup' in check_function.__code__.co_varnames else check_function(url)
        results[rule] = result
    
    return results

# Generate a report based on the analysis
def generate_report(url):
    results = analyze_webpage(url)
    if not results:
        return "Error analyzing the webpage."
    
    report = f"UX Analysis Report for {url}:\n\n"
    for rule, passed in results.items():
        if passed:
            report += f"✔ {rule}\n"
        else:
            report += f"✘ {rule} (Needs improvement)\n"
    
    return report

# Input the webpage URL to analyze
if __name__ == "__main__":
    url = input("Enter the webpage URL to analyze: ")
    report = generate_report(url)
    print(report)
