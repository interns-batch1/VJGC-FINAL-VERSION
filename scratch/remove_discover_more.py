import os
import re

templates_dir = r'c:\Users\Admin\vjgc-final\vjs-website\templates'

# Pattern to match the divider and the link block
# We use re.DOTALL to match across multiple lines and \s* for varying whitespace
pattern = re.compile(
    r'<div class="card-footer-divider"></div>\s*<a href="#" class="discover-more-link">.*?</a>',
    re.DOTALL
)

def remove_discover_more(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = pattern.sub('', content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

if __name__ == "__main__":
    count = 0
    for filename in os.listdir(templates_dir):
        if filename.endswith('.html'):
            file_path = os.path.join(templates_dir, filename)
            if remove_discover_more(file_path):
                print(f"Updated {filename}")
                count += 1
    print(f"Total files updated: {count}")
