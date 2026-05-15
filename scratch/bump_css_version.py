import os
import re

templates_dir = r"c:\Users\Admin\vjgc-final\vjs-website\templates"

for filename in os.listdir(templates_dir):
    if filename.endswith(".html"):
        filepath = os.path.join(templates_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Bump custom.css version from v=1.0 to v=1.1
        new_content = content.replace('custom.css?v=1.0', 'custom.css?v=1.1')
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Bumped version in {filename}")
