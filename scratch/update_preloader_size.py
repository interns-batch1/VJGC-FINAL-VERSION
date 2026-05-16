import os
import re

def update_preloader():
    target_dirs = [
        'c:/Users/Admin/vjgc-final/vjs-website',
        'c:/Users/Admin/vjgc-final/vjs-website/templates'
    ]

    # Patterns to find and update
    # 1. Update .logo-circle width, height, and padding
    logo_circle_pattern = r'(\.logo-circle\s*\{[^}]*width:\s*)100px(;[^}]*height:\s*)100px(;[^}]*padding:\s*)18px'
    logo_circle_replacement = r'\1120px\2120px\314px'

    # 2. Update .pulse-ring width and height (optional, but let's keep them synced if needed)
    # The user said keep pulsing rings unchanged, so I'll leave them at 100px so they emerge from behind the 120px circle.
    
    # Actually, let's check if the user wants the rings to also be larger. 
    # "Keep everything else exactly the same — the pulsing rings ... should remain unchanged."
    # So I will NOT change the pulse-ring size. They will start at 100px (hidden) and emerge.

    for directory in target_dirs:
        if not os.path.exists(directory):
            continue
            
        for filename in os.listdir(directory):
            if filename.endswith('.html') and not filename.endswith('.bak'):
                filepath = os.path.join(directory, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Check if we have the styles
                new_content = re.sub(logo_circle_pattern, logo_circle_replacement, content, flags=re.DOTALL)
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated preloader styles in {filename}")

if __name__ == "__main__":
    update_preloader()
