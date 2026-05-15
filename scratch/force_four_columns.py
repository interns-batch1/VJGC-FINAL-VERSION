import os
import re

templates_dir = r'c:\Users\Admin\vjgc-final\vjs-website\templates'

def force_four_columns(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Isolate the "Our Business" section
    parts = re.split(r'(<!--\s*Our Businesses Section\s*-->|<section class="biz-section-v2">)', content, flags=re.IGNORECASE)
    
    changed = False
    new_parts = []
    in_biz = False
    
    for part in parts:
        if re.search(r'Our Businesses Section|biz-section-v2', part, re.IGNORECASE):
            in_biz = True
            new_parts.append(part)
        elif in_biz:
            # Look for the first row in this section
            if '<div class="row' in part:
                # Replace the row class to include row-cols-lg-4
                # and ensure children are col-lg-3
                part = re.sub(r'<div class="row([^"]*)"', r'<div class="row\1 row-cols-lg-4"', part, count=1)
                part = part.replace('col-lg-4', 'col-lg-3')
                changed = True
            new_parts.append(part)
            # We don't reset in_biz here because a section might have multiple rows or nested structures
            # but usually it's one row per section.
        else:
            new_parts.append(part)
            
    if changed:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write("".join(new_parts))
        return True
    return False

if __name__ == "__main__":
    count = 0
    for filename in os.listdir(templates_dir):
        if filename.endswith('.html'):
            file_path = os.path.join(templates_dir, filename)
            if force_four_columns(file_path):
                print(f"Updated {filename}")
                count += 1
    print(f"Total files updated: {count}")
