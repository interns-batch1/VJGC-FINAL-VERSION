import os
import re
import glob

template_dir = r'c:\Users\Admin\vjgc-final\vjs-website\templates'
html_files = glob.glob(os.path.join(template_dir, '**/*.html'), recursive=True)

# Pattern for the dropdown
dropdown_pattern_no_comment = re.compile(
    r'(?:<!--\s*Language Dropdown\s*-->\s*)?<div class="vjs-nav-action dropdown[^>]*>\s*<button[^>]*>.*?vjs-lang-label.*?</button>\s*<ul[^>]*vjs-lang-menu[^>]*>.*?</ul>\s*</div>', 
    re.DOTALL | re.IGNORECASE
)

# Pattern for the script
google_translate_pattern = re.compile(
    r'<div id="google_translate_element" style="display:none;"></div>\s*<script type="text/javascript"\s*src="https://translate\.google\.com/translate_a/element\.js\?cb=googleTranslateElementInit"></script>', 
    re.DOTALL | re.IGNORECASE
)

modified_files = 0
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    # Remove language dropdown
    new_content = dropdown_pattern_no_comment.sub('', new_content)
    
    # Remove google translate script
    new_content = google_translate_pattern.sub('', new_content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        modified_files += 1

print(f'Modified {modified_files} files.')
