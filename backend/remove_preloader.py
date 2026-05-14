import os
import re

def remove_preloader():
    templates_dir = 'templates'
    if not os.path.exists(templates_dir):
        print(f"Directory {templates_dir} not found.")
        return

    # Patterns to match the preloader block we've been using
    patterns = [
        r'<!--\s*===================================================\s*Loading Transition\s*====================================================\s*-->\s*<div id="preloader".*?</div>\s*</div>',
        r'<!--\s*Loading Transition\s*-->.*?<div id="preloader">.*?</div>\s*</div>',
        r'<div id="preloader">.*?</div>\s*</div>',
        r'<!--\s*Loading Transition\s*-->.*?<div id="preloader">.*?</div>',
        r'<div id="preloader">.*?</div>'
    ]

    for filename in os.listdir(templates_dir):
        if filename.endswith('.html'):
            filepath = os.path.join(templates_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = content
            for pattern in patterns:
                new_content = re.sub(pattern, '', new_content, flags=re.DOTALL)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Removed preloader from {filename}")

if __name__ == "__main__":
    remove_preloader()
