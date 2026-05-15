import os
import re

directory = r'c:\Users\Admin\vjgc-final\vjs-website\templates'
bootstrap_icons_link = '	<!-- Bootstrap Icons -->\n	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">\n'

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already has bootstrap icons
        if 'bootstrap-icons.min.css' in content:
            continue
            
        # Insert before </head> or after custom.css
        if '<link rel="stylesheet" type="text/css" href="{{ url_for(\'static\', filename=\'css/custom.css\') }}' in content:
            # Find the line with custom.css and insert after it
            pattern = r'(<link rel="stylesheet" type="text/css" href="{{ url_for\(\'static\', filename=\'css/custom\.css\'\) }}.*?>)'
            new_content = re.sub(pattern, r'\1\n' + bootstrap_icons_link, content)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
        elif '</head>' in content:
            new_content = content.replace('</head>', bootstrap_icons_link + '</head>')
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename} (via </head>)")
