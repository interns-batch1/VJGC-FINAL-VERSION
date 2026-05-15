import os
import re

templates_dir = r"c:\Users\Admin\vjgc-final\vjs-website\templates"
files_to_fix = [
    "export-import.html",
    "logistics-services.html",
    "it-consulting.html",
    "green-energy.html",
    "it-training.html",
    "plantations.html",
    "property-services.html",
    "travel-rentals.html",
    "yoga-wellness.html"
]

for filename in files_to_fix:
    filepath = os.path.join(templates_dir, filename)
    if not os.path.exists(filepath):
        print(f"Skipping {filename}, not found.")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern: {% if cms['Our Business'] ... %} ... {% for ... %} ... {% endfor %}</section>
    # We need to add {% endif %} after {% endfor %} but before </section>
    
    # Specifically looking for the pattern where it's missing the endif
    pattern = r"({% for card in cms\['Our Business'\]\.content %}.*?{% endfor %})(</section>)"
    
    if "{% if cms['Our Business']" in content and "{% endif %}" not in content.split("{% if cms['Our Business']")[1].split("</section>")[0]:
        new_content = re.sub(pattern, r"\1{% endif %}\2", content, flags=re.DOTALL)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed {filename}")
        else:
            print(f"Could not find pattern in {filename}")
    else:
        print(f"{filename} seems already correct or doesn't have the block.")

print("Done.")
