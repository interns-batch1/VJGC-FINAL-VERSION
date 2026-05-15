import os

templates_dir = r"c:\Users\Admin\vjgc-final\vjs-website\templates"
files_to_fix = [
    "logistics-services.html",
    "green-energy.html",
    "it-training.html",
    "plantations.html",
    "property-services.html",
    "travel-rentals.html",
    "yoga-wellness.html"
]

target = "{% endfor %}</section>"
replacement = "{% endfor %}\n\t\t\t\t\t\t{% endif %}\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</section>"

for filename in files_to_fix:
    filepath = os.path.join(templates_dir, filename)
    if not os.path.exists(filepath):
        print(f"Skipping {filename}, not found.")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if target in content:
        new_content = content.replace(target, replacement)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {filename}")
    else:
        print(f"Target not found in {filename}")

print("Done.")
