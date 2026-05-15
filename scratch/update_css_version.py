import os
import re

TEMPLATE_DIR = r'c:\Users\Admin\vjgc-final\vjs-website\templates'

# Regex to match custom.css link with or without existing version
# Matches: href="{{ url_for('static', filename='css/custom.css') }}?v=1.0"
# Or: href="{{ url_for('static', filename='css/custom.css') }}"
CSS_PATTERN = r'href="{{ url_for\(\'static\', filename=\'css/custom.css\'\) }}(?:\?v=[\d\.]+)*"'
NEW_HREF = 'href="{{ url_for(\'static\', filename=\'css/custom.css\') }}?v=1.1"'

for filename in os.listdir(TEMPLATE_DIR):
    if filename.endswith('.html'):
        filepath = os.path.join(TEMPLATE_DIR, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = re.sub(CSS_PATTERN, NEW_HREF, content)
            
            # Handle double quote variation
            CSS_PATTERN_DQ = r'href="{{ url_for\("static", filename="css/custom.css"\) }}(?:\?v=[\d\.]+)*"'
            new_content = re.sub(CSS_PATTERN_DQ, NEW_HREF, new_content)

            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated version in {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
