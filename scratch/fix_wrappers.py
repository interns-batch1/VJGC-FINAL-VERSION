import os

templates_dir = r"c:\Users\Admin\vjgc-final\vjs-website\templates"
files_to_fix = [
    "data-centers-hosting.html",
    "export-import.html",
    "logistics-services.html",
    "it-training.html",
    "it-consulting.html",
    "green-energy.html",
    "yoga-wellness.html",
    "travel-rentals.html",
    "property-services.html",
    "plantations.html"
]

for filename in files_to_fix:
    filepath = os.path.join(templates_dir, filename)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for missing closing tags
    # Usually we want to close them before the scripts
    if "light-bg-page-wrapper" in content and "<!-- /.light-bg-page-wrapper -->" not in content:
        # Find where to insert closing tags
        # A good place is before the first <script> after the footer
        if "</footer>" in content:
            parts = content.split("</footer>")
            if len(parts) > 1:
                # Add the closing divs
                new_content = parts[0] + "</footer>\n\t</div> <!-- /.light-bg-page-wrapper -->\n</div> <!-- /.main-page-wrapper -->" + parts[1]
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Fixed wrappers in {filename}")
            else:
                print(f"Footer split failed in {filename}")
        else:
            print(f"No footer found in {filename}")
    else:
        print(f"{filename} already correct or no wrapper found.")

print("Done.")
