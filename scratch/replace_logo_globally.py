import os
import re

directory = r'c:\Users\Admin\vjgc-final\vjs-website\templates'
logo_html = '''								<div class="logo-icon-circle">
									<img src="{{ url_for(\'static\', filename=\'images/logo/vijayalakshmi-mark.png\') }}" alt="VJS Logo" style="width: 100%; height: 100%; object-fit: contain; border-radius: 50%;">
								</div>'''

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if it has the old logo block
        if '<div class="logo-icon-circle">' in content and '<i class="bi bi-crown-fill"></i>' in content:
            # Replace the whole logo-icon-circle block
            pattern = r'<div class="logo-icon-circle">.*?<i class="bi bi-crown-fill"></i>.*?</div>'
            new_content = re.sub(pattern, logo_html, content, flags=re.DOTALL)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated logo in {filename}")
