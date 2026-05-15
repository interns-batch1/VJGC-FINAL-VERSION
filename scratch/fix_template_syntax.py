import os
import re

def fix_template_syntax(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html') and file != 'index-2.html':
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Fix "Our Businesses" section syntax
                # The section usually starts with {% if cms['Our Business'] ... %}
                # and ends with </section>
                
                # Check if endfor/endif are missing before </section>
                section_blocks = re.findall(r'({% if cms\[\'Our Business\'\].*?)(</section>)', content, re.DOTALL)
                
                new_content = content
                for start_part, end_tag in section_blocks:
                    if '{% endfor %}' not in start_part or '{% endif %}' not in start_part:
                        # Reconstruct the section properly
                        # Find the last closing div of the card and add the missing tags
                        
                        # Looking for the last card div closure
                        # This is tricky, but let's try to find the last </div> before </section>
                        
                        # A better way: just ensure the tags are there before </section>
                        # In my previous repair, I put the card inside a loop but forgot to close it properly in the replacement string
                        
                        fixed_block = start_part.strip()
                        if '{% endfor %}' not in fixed_block:
                            fixed_block += '\n\t\t\t\t\t\t{% endfor %}'
                        if '{% endif %}' not in fixed_block:
                            fixed_block += '\n\t\t\t\t\t\t{% endif %}\n\t\t\t\t\t</div>\n\t\t\t\t</div>'
                        
                        new_content = new_content.replace(start_part, fixed_block)

                # Fix "At a Glance" section syntax
                glance_blocks = re.findall(r'({% if cms\[\'At a Glance\'\].*?)(</section>)', new_content, re.DOTALL)
                for start_part, end_tag in glance_blocks:
                    if '{% endfor %}' not in start_part or '{% endif %}' not in start_part:
                        fixed_block = start_part.strip()
                        if '{% endfor %}' not in fixed_block:
                            fixed_block += '\n\t\t\t\t\t\t{% endfor %}'
                        if '{% endif %}' not in fixed_block:
                            fixed_block += '\n\t\t\t\t\t\t{% endif %}\n\t\t\t\t\t</div>\n\t\t\t\t</div>'
                        new_content = new_content.replace(start_part, fixed_block)

                # Clean up duplicated row classes (just in case)
                new_content = re.sub(r'class="row (vjs-card-row\s*)+', 'class="row vjs-card-row ', new_content)

                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Fixed syntax in {file}")

if __name__ == "__main__":
    fix_template_syntax(r'c:\Users\Admin\vjgc-final\vjs-website\templates')
