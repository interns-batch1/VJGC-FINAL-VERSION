import os
import re

def final_restoration():
    new_preloader = """	<div class="main-page-wrapper">
		<div id="preloader">
			<div class="preloader-content">
				<div class="logo-container">
					<div class="pulse-ring"></div>
					<div class="pulse-ring"></div>
					<div class="pulse-ring"></div>
					<div class="logo-circle">
						<img src="{{ url_for('static', filename='images/logo/vijayalakshmi-mark.png') }}?v=1.0" alt="VJS Logo">
					</div>
				</div>
				<div class="brand-text">
					<div class="brand-main">VIJAYALAKSHMI GROUP</div>
					<div class="brand-sub">OF COMPANIES</div>
				</div>
				<div class="loading-bar-container">
					<div class="loading-bar-fill"></div>
				</div>
				<div class="loading-text">LOADING</div>
			</div>
		</div>
"""

    target_dirs = [
        'c:/Users/Admin/vjgc-final/vjs-website/templates'
    ]

    for directory in target_dirs:
        for filename in os.listdir(directory):
            if filename.endswith('.html'):
                filepath = os.path.join(directory, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Find the Body tag
                body_match = re.search(r'<body.*?>', content, flags=re.IGNORECASE)
                if not body_match:
                    continue
                
                # Find the Header tag (or the Theme Main Menu comment)
                header_match = re.search(r'(<!--\s*==+\s*Theme Main Menu|<header)', content, flags=re.IGNORECASE)
                if not header_match:
                    continue

                # Everything between <body> and <header> is replaced with the new preloader block
                # This fixes all duplicates, unclosed divs, and extra wrappers.
                new_content = content[:body_match.end()] + "\n" + new_preloader + "\n\t\t" + content[header_match.start():]
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Restored {filename}")

if __name__ == "__main__":
    final_restoration()
