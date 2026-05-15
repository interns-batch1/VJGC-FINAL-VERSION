import os

def remove_old_footer(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # We want to remove the block between lines 2121 and 2383 (approximately)
    # But line numbers shifted since I already removed some lines.
    
    # I'll look for the markers
    start_marker = '					/* INNER CONTAINER */'
    end_marker = '			</footer>'
    
    new_lines = []
    skip = False
    for line in lines:
        if start_marker in line:
            skip = True
        
        if not skip:
            new_lines.append(line)
            
        if skip and end_marker in line:
            # We found the end of the block we want to remove
            # But wait! There are multiple </footer> tags.
            # The one we want is the one BEFORE "Optional JavaScript"
            # I'll check the next line
            pass
            
    # That's too risky. I'll just use a more precise string matching.
    
    content = "".join(lines)
    
    # Match the block exactly
    import re
    # We want the block that starts with /* INNER CONTAINER */ and ends with </footer>\n\n\n\t\t\t<!-- Optional JavaScript
    pattern = re.compile(r'\s*/\* INNER CONTAINER \*/.*?</footer>', re.DOTALL)
    
    new_content = pattern.sub('', content, count=1)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == "__main__":
    remove_old_footer(r'c:\Users\Admin\vjgc-final\vjs-website\templates\index-2.html')
