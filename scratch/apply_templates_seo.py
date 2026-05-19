import re
import os
import glob

templates_dir = r"c:\Users\Admin\vjgc-final\vjs-website\templates"
html_files = glob.glob(os.path.join(templates_dir, "*.html"))

# Define patterns to remove
patterns = [
    r'<meta\s+name=["\']keywords["\'][^>]*>',
    r'<meta\s+name=["\']description["\'][^>]*>',
    r'<meta\s+property=["\']og:site_name["\'][^>]*>',
    r'<meta\s+property=["\']og:url["\'][^>]*>',
    r'<meta\s+property=["\']og:type["\'][^>]*>',
    r'<meta\s+property=["\']og:title["\'][^>]*>',
    r'<meta\s+property=["\']og:description["\'][^>]*>',
    r'<meta\s+name=["\']og:image["\'][^>]*>',
    r'<meta\s+property=["\']og:image["\'][^>]*>',
    r'<meta\s+name=["\']twitter:card["\'][^>]*>',
    r'<meta\s+name=["\']twitter:url["\'][^>]*>',
    r'<meta\s+name=["\']twitter:title["\'][^>]*>',
    r'<meta\s+name=["\']twitter:description["\'][^>]*>',
    r'<meta\s+name=["\']twitter:image["\'][^>]*>',
    r'<meta\s+name=["\']robots["\'][^>]*>',
    r'<link\s+rel=["\']canonical["\'][^>]*>',
    r'<title>.*?</title>'
]

seo_block = """
	<meta name="keywords" content="{{ seo.keywords if seo else '' }}">
	<meta name="description" content="{{ seo.description if seo else '' }}">
	<link rel="canonical" href="{{ seo.canonical_url or request.url }}">
	<meta name="robots" content="{{ seo.robots or 'index, follow' }}">
	<meta property="og:site_name" content="Vijayalakshmi Group Of Companies">
	<meta property="og:url" content="{{ seo.og_url or request.url }}">
	<meta property="og:type" content="website">
	<meta property="og:title" content="{{ seo.og_title or (seo.title if seo else '') }}">
	<meta property="og:description" content="{{ seo.og_description or (seo.description if seo else '') }}">
	<meta property="og:image" content="{{ seo.og_image or url_for('static', filename='images/logo/vijayalakshmi-mark.png') }}?v=1.2">
	<meta name="twitter:card" content="summary_large_image">
	<meta name="twitter:url" content="{{ seo.og_url or request.url }}">
	<meta name="twitter:title" content="{{ seo.og_title or (seo.title if seo else '') }}">
	<meta name="twitter:description" content="{{ seo.og_description or (seo.description if seo else '') }}">
	<meta name="twitter:image" content="{{ seo.og_image or url_for('static', filename='images/logo/vijayalakshmi-mark.png') }}?v=1.2">
	<title>{{ seo.title if seo else 'Vijayalakshmi Group of Companies' }}</title>
"""

updated_count = 0
skipped_count = 0

for file_path in html_files:
    file_name = os.path.basename(file_path)
    
    # Skip backup files or specific pages we don't want to auto-modify
    if "bak" in file_name or file_name == "new_brand_sections.html":
        print(f"Skipping backup/ignored file: {file_name}")
        skipped_count += 1
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check if the file already uses dynamic SEO templates
    if "seo.keywords" in content or "seo.title" in content:
        # Check if it has hardcoded elements or already dynamic
        # index-2.html and media-release.html already have dynamic SEO
        if file_name in ["index-2.html", "media-release.html"]:
            print(f"Skipping already dynamic page: {file_name}")
            skipped_count += 1
            continue
            
    # Apply replacements
    modified = content
    for pattern in patterns:
        modified = re.sub(pattern, '', modified, flags=re.IGNORECASE | re.DOTALL)
        
    # Insert new SEO block right after <head>
    modified = re.sub(r'<head>', f'<head>\n{seo_block}', modified, flags=re.IGNORECASE)
    
    # Save the updated file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(modified)
        
    print(f"Updated SEO tags in: {file_name}")
    updated_count += 1

print(f"\nProcessing complete! Updated {updated_count} files, skipped {skipped_count} files.")
