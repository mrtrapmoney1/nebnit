import os
from datetime import datetime
from bs4 import BeautifulSoup

# --- Configuration ---
BASE_URL = "https://metrotv-audiotech.com"
# Add files you want to exclude from the sitemap
EXCLUDE_FILES = ['competitors.html'] 
# --- End Configuration ---

def get_page_title(filepath):
    """Extracts the <title> from an HTML file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
            if soup.title and soup.title.string:
                return soup.title.string.strip()
    except Exception as e:
        print(f"Could not read title from {filepath}: {e}")
    return None

def create_sitemap():
    """
    Generates a sitemap.xml file by scanning the current directory for .html files.
    """
    urls = []
    # Scan the current directory for .html files
    for filename in os.listdir('.'):
        if filename.endswith(".html") and filename not in EXCLUDE_FILES:
            filepath = os.path.join('.', filename)
            
            # Get the last modification time of the file
            last_mod_timestamp = os.path.getmtime(filepath)
            last_mod_date = datetime.fromtimestamp(last_mod_timestamp).strftime('%Y-%m-%d')
            
            # Set priority based on filename
            priority = "1.0" if filename == "index.html" else "0.8"
            
            url_data = {
                'loc': f"{BASE_URL}/{filename}",
                'lastmod': last_mod_date,
                'priority': priority
            }
            urls.append(url_data)

    # Generate the XML content
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for url in urls:
        xml_content += '  <url>\n'
        xml_content += f"    <loc>{url['loc']}</loc>\n"
        xml_content += f"    <lastmod>{url['lastmod']}</lastmod>\n"
        xml_content += f"    <priority>{url['priority']}</priority>\n"
        xml_content += '  </url>\n'
    xml_content += '</urlset>'

    # Write the content to sitemap.xml
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(xml_content)
    
    print("✅ Sitemap.xml generated successfully!")
    print(f"Found {len(urls)} pages.")

if __name__ == "__main__":
    # You will need to install BeautifulSoup: pip install beautifulsoup4
    create_sitemap()
