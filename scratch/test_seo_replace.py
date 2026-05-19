import re
import os

template_path = r"c:\Users\Admin\vjgc-final\vjs-website\templates\about-us-v1.html"

with open(template_path, 'r', encoding='utf-8') as f:
    content = f.read()

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

modified = content
for pattern in patterns:
    modified = re.sub(pattern, '', modified, flags=re.IGNORECASE | re.DOTALL)

# Now, insert the new dynamic SEO block right after <head>
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

# Insert after <head>
modified = re.sub(r'<head>', f'<head>\n{seo_block}', modified, flags=re.IGNORECASE)

print("Original Head segment:")
head_start = content.lower().find("<head>")
print(content[head_start:head_start+500])

print("\nModified Head segment:")
head_start_mod = modified.lower().find("<head>")
print(modified[head_start_mod:head_start_mod+1500])
