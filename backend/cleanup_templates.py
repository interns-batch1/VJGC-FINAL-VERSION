import os
import re

def cleanup_templates():
    templates_dir = 'templates'
    
    # This pattern matches the leftover transition comments and extra divs 
    # that were often part of the preloader injection area.
    pattern = r'<!-- =+.*?Loading Transition.*?=+ -->\s*'
    
    for filename in os.listdir(templates_dir):
        if filename.endswith('.html'):
            filepath = os.path.join(templates_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Remove leftover comments
            new_content = re.sub(pattern, '', content, flags=re.DOTALL)
            
            # Remove the specific leftover div structure in index-2.html and others
            # Look for </div> tags followed by nothing but whitespace before the next comment or header
            # But only in the area where the preloader was (right after main-page-wrapper)
            
            # Safely remove up to 3 closing divs that are immediately followed by each other after main-page-wrapper
            split_tag = '<div class="main-page-wrapper">'
            if split_tag in new_content:
                parts = new_content.split(split_tag, 1)
                after = parts[1]
                # Match consecutive </div> tags and whitespace at the beginning of 'after'
                after = re.sub(r'^\s*(</div>\s*){1,3}', '', after)
                new_content = parts[0] + split_tag + after

            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Cleaned up {filename}")

if __name__ == "__main__":
    cleanup_templates()
