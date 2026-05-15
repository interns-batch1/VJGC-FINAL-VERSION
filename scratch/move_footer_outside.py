import os
import re

def fix_footer_nesting(directory):
    footer_pattern = re.compile(r'(<!--\s*Footer\s*-->\s*<footer class="footer-vjs-premium">.*?</footer>|<footer class="footer-vjs-premium">.*?</footer>)', re.DOTALL)
    
    # More flexible wrapper closing pattern
    wrapper_close_patterns = [
        re.compile(r'(</div>\s*<!--\s*/\.main-page-wrapper\s*-->)'),
        re.compile(r'(</div>\s*<!--\s*main-page-wrapper\s*-->)'),
        re.compile(r'(</div>\s*<!--\s*/\s*main-page-wrapper\s*-->)'),
        re.compile(r'(</div>\s*<!--\s*\.main-page-wrapper\s*-->)')
    ]

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                footer_match = footer_pattern.search(content)
                if footer_match:
                    footer_content = footer_match.group(1)
                    
                    # Remove footer from its current position
                    temp_content = content.replace(footer_content, '')
                    
                    # Try to find the wrapper closing tag
                    wrapper_match = None
                    for pattern in wrapper_close_patterns:
                        wrapper_match = pattern.search(temp_content)
                        if wrapper_match:
                            break
                    
                    if wrapper_match:
                        # Insert footer AFTER the wrapper closing tag
                        insertion_point = wrapper_match.end()
                        final_content = temp_content[:insertion_point] + "\n\n" + footer_content + temp_content[insertion_point:]
                        
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(final_content)
                        print(f"Fixed footer in {file}")
                    else:
                        # If no comment found, try to find the LAST closing div before scripts
                        # But this is risky. Let's just log it.
                        print(f"Could not find wrapper closing tag in {file}")

if __name__ == "__main__":
    templates_dir = r'c:\Users\Admin\vjgc-final\vjs-website\templates'
    fix_footer_nesting(templates_dir)
