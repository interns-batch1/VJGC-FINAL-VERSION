import os
import re

def fix_corruption_and_apply_correctly():
    target_dirs = [
        'c:/Users/Admin/vjgc-final/vjs-website',
        'c:/Users/Admin/vjgc-final/vjs-website/templates'
    ]

    # Pattern to match the corrupted string
    # corrupted: J0pxŠ0pxÌpx;
    # It was supposed to be: width: 120px; height: 120px; padding: 14px;
    # (The regex groups captured "width: ", "; height: ", "; padding: ")
    
    # Let's use a more robust way to find the .logo-circle block and replace it entirely
    correct_block = """.logo-circle {
			width: 120px;
			height: 120px;
			border: 1px solid rgba(220, 38, 38, 0.2);
			border-radius: 50%;
			padding: 14px;"""

    corruption_pattern = r'\.logo-circle\s*\{[^}]*J0pxŠ0pxÌpx'

    for directory in target_dirs:
        if not os.path.exists(directory):
            continue
            
        for filename in os.listdir(directory):
            if filename.endswith('.html'):
                filepath = os.path.join(directory, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                if 'J0pxŠ0pxÌpx' in content:
                    new_content = re.sub(corruption_pattern, correct_block, content, flags=re.DOTALL)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Fixed and updated: {filename}")

if __name__ == "__main__":
    fix_corruption_and_apply_correctly()
