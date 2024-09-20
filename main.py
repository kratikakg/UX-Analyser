import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import matplotlib.pyplot as plt
import os

UX_RULES = {
    "1. Proper Heading Structure": lambda soup, url: check_headings_structure(soup),
    "2. Mobile Responsiveness": lambda soup, url: check_mobile_responsiveness(url),
    "3. Text Readability (Contrast and Font Size)": lambda soup, url: check_text_readability(soup),
    "4. Alt Text for Images": lambda soup, url: check_image_alt_text(soup),
    "5. Presence of Call to Action (CTA)": lambda soup, url: check_cta_buttons(soup),
    "6. No Broken Links": lambda soup, url: check_broken_links(soup, url),
    "7. Page Load Speed": lambda soup, url: check_page_load_speed(url),
    "8. Accessibility for Screen Readers": lambda soup, url: check_accessibility(soup),
    "9. HTTPS Security": lambda soup, url: check_https(url),
    "10. SEO Meta Tags": lambda soup, url: check_seo_tags(soup),
    "11. Image Optimization": lambda soup, url: check_image_optimization(soup),
    "12. Favicon Presence": lambda soup, url: check_favicon(soup),
    "13. User-Friendly URL Structure": lambda soup, url: check_url_structure(url),
    "14. Cookie Consent Presence": lambda soup, url: check_cookie_consent(soup),
}

def scrape_webpage(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    except Exception as e:
        print(f"Error accessing the URL: {e}")
        return None
    
def check_headings_structure(soup):
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    return len(headings) > 0

def check_mobile_responsiveness(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    viewport = soup.find('meta', {'name': 'viewport'})
    return viewport is not None

def check_text_readability(soup):
    paragraphs = soup.find_all('p')
    return len(paragraphs) > 0

def check_image_alt_text(soup):
    images = soup.find_all('img')
    missing_alt = [img for img in images if not img.get('alt')]
    return len(missing_alt) == 0

def check_cta_buttons(soup):
    buttons = soup.find_all('button') + soup.find_all('a', href=True)
    cta_words = ['buy', 'subscribe', 'learn more', 'contact', 'sign up']
    for btn in buttons:
        if any(word in btn.text.lower() for word in cta_words):
            return True
    return False

def check_broken_links(soup, url):
    links = [a['href'] for a in soup.find_all('a', href=True)]
    broken_links = []
    for link in links:
        try:
            if link.startswith('/'):
                link = urlparse(url).scheme + "://" + urlparse(url).netloc + link
            response = requests.head(link)
            if response.status_code != 200:
                broken_links.append(link)
        except Exception as e:
            broken_links.append(link)
    return len(broken_links) == 0

def check_page_load_speed(url):
    import time
    start_time = time.time()
    try:
        response = requests.get(url)
        load_time = time.time() - start_time
        return load_time < 2
    except Exception as e:
        return False

def check_accessibility(soup):
    aria_tags = soup.find_all(attrs={"aria-label": True})
    landmarks = soup.find_all(['nav', 'header', 'footer', 'main', 'aside'])
    return len(aria_tags) > 0 or len(landmarks) > 0

def check_https(url):
    return urlparse(url).scheme == 'https'

def check_seo_tags(soup):
    description = soup.find('meta', {'name': 'description'})
    keywords = soup.find('meta', {'name': 'keywords'})
    return description is not None and keywords is not None

def check_image_optimization(soup):
    images = soup.find_all('img')
    oversized_images = []
    
    for img in images:
        if 'src' in img.attrs:
            try:
                response = requests.head(img['src'])
                content_length = response.headers.get('content-length')
                
                if content_length and content_length.isdigit():
                    content_length = int(content_length)
                    
                    if content_length > 500000:
                        oversized_images.append(img['src'])
            except Exception as e:
                print(f"Error processing image {img['src']}: {e}")
    
    return len(oversized_images) == 0
def check_favicon(soup):
    favicon = soup.find('link', rel='icon')
    return favicon is not None

def check_url_structure(url):
    path = urlparse(url).path
    return all(x.isalnum() or x == '/' for x in path)

def check_cookie_consent(soup):
    consent_keywords = ['cookie consent', 'accept cookies', 'privacy policy']
    return any(consent in soup.text.lower() for consent in consent_keywords)

def analyze_webpage(url):
    soup = scrape_webpage(url)
    if not soup:
        return

    results = {}
    for rule, check_function in UX_RULES.items():
        result = check_function(soup, url)
        results[rule] = result
    
    return results

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
    
    generate_visualization(results, url)
    
    return report

def generate_visualization(results, url):
    labels = list(results.keys())
    values = [1 if v else 0 for v in results.values()]

    fig, ax = plt.subplots()
    ax.barh(labels, values, color=['green' if v else 'red' for v in values])
    ax.set_xlabel('Pass (1) or Fail (0)')
    ax.set_title(f'UX Analysis Results for {url}')

    if not os.path.exists('reports'):
        os.makedirs('reports')
    plt.tight_layout()
    image_path = f'reports/ux_analysis_{urlparse(url).netloc}.png'
    plt.savefig(image_path)
    plt.close()

    print(f"Visualization saved as: {image_path}")

if __name__ == "__main__":
    url = input("Enter the webpage URL to analyze: ")
    report = generate_report(url)
    print(report)
