import os
import re

templates_dir = r"c:\Users\Admin\vjgc-final\vjs-website\templates"

updated_count = 0
for filename in os.listdir(templates_dir):
    if filename.endswith(".html"):
        filepath = os.path.join(templates_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        original_content = content
        
        # Replace style.min.css') }}?v=1.0 or style.min.css')}}?v=1.0 with style.min.css') }}?v=1.1
        content = re.sub(
            r"style\.min\.css\'\)\s*\}\}\?v=1\.0",
            "style.min.css') }}?v=1.1",
            content
        )
        # Also replace style.min.css") }}?v=1.0
        content = re.sub(
            r"style\.min\.css\"\)\s*\}\}\?v=1\.0",
            "style.min.css') }}?v=1.1",
            content
        )
        
        # Replace style.min.css') }} with style.min.css') }}?v=1.1 if it does not have a query string
        # Match style.min.css') }} or style.min.css')}} not followed by ?v=
        content = re.sub(
            r"style\.min\.css\'\)\s*\}\}(?!\?v=)",
            "style.min.css') }}?v=1.1",
            content
        )
        content = re.sub(
            r"style\.min\.css\"\)\s*\}\}(?!\?v=)",
            "style.min.css') }}?v=1.1",
            content
        )
        
        # Specific fix for: href="{{ url_for('static', filename='css/') }}style.min.css"
        content = re.sub(
            r"href\s*=\s*[\"\']\{\{\s*url_for\(\'static\'\s*,\s*filename=\'css/\'\)\s*\}\}style\.min\.css[\"\']",
            "href=\"{{ url_for('static', filename='css/style.min.css') }}?v=1.1\"",
            content
        )

        if content != original_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated style.min.css version in: {filename}")
            updated_count += 1

print(f"Done! Updated {updated_count} files.")
