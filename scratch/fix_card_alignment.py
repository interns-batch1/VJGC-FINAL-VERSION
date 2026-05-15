import os
import re

templates_dir = r'c:\Users\Admin\vjgc-final\vjs-website\templates'

# Pattern to find the "Our Businesses" section and then the col-lg-4 within it
# We search for the comment or the section-title, then the following col-lg-4
pattern = re.compile(
    r'(<!--\s*Our Businesses Section\s*-->.*?<section class="biz-section-v2">.*?col-lg-)4',
    re.DOTALL | re.IGNORECASE
)

# Alternative pattern for sections that might not have the comment or have a different class
pattern2 = re.compile(
    r'(<h2 class="section-title">.*?Our Business.*?</h2>.*?<div class="row.*?>.*?col-lg-)4',
    re.DOTALL | re.IGNORECASE
)

def fix_card_alignment(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We need to replace all occurrences of col-lg-4 with col-lg-3 
    # but ONLY within the "Our Business" sections.
    
    # Split the content by sections to isolate "Our Business"
    sections = re.split(r'(<!--\s*Our Businesses Section\s*-->|<section class="biz-section-v2">)', content, flags=re.IGNORECASE)
    
    changed = False
    new_content_parts = []
    
    in_biz_section = False
    for part in sections:
        if re.search(r'Our Businesses Section|biz-section-v2', part, re.IGNORECASE):
            in_biz_section = True
            new_content_parts.append(part)
        elif in_biz_section:
            # Check if this part contains the cards
            if 'col-lg-4' in part:
                part = part.replace('col-lg-4', 'col-lg-3')
                changed = True
            new_content_parts.append(part)
            # We assume the next section or end of file terminates the biz section
            # However, for safety in this simple script, we'll just keep it simple 
            # and let it process until the next main section if any.
        else:
            new_content_parts.append(part)
            
    if changed:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write("".join(new_content_parts))
        return True
    return False

if __name__ == "__main__":
    count = 0
    for filename in os.listdir(templates_dir):
        if filename.endswith('.html'):
            file_path = os.path.join(templates_dir, filename)
            if fix_card_alignment(file_path):
                print(f"Updated {filename}")
                count += 1
    print(f"Total files updated: {count}")
