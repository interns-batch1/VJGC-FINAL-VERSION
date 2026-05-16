import os
import re

def update_preloader_color():
    target_dirs = [
        'c:/Users/Admin/vjgc-final/vjs-website',
        'c:/Users/Admin/vjgc-final/vjs-website/templates'
    ]

    # Pattern to find .brand-main color
    # Currently: color: #c5a059;
    pattern = r'(\.brand-main\s*\{[^}]*color:\s*)#c5a059'
    replacement = r'\1#dc2626' # Vibrant red to match the rings

    for directory in target_dirs:
        if not os.path.exists(directory):
            continue
            
        for filename in os.listdir(directory):
            if filename.endswith('.html') and not filename.endswith('.bak'):
                filepath = os.path.join(directory, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                if '.brand-main' in content:
                    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
                    if new_content != content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Updated brand color in {filename}")

if __name__ == "__main__":
    update_preloader_color()
