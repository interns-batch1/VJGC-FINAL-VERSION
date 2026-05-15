import os
import re

def fix_preloader_mess():
    # Define the CORRECT new HTML
    # Note: Added the missing closing div and ensured proper indentation
    new_html = """		<div id="preloader">
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
		</div>"""

    target_dirs = [
        'c:/Users/Admin/vjgc-final/vjs-website',
        'c:/Users/Admin/vjgc-final/vjs-website/templates'
    ]

    for directory in target_dirs:
        if not os.path.exists(directory):
            continue
            
        for filename in os.listdir(directory):
            if filename.endswith('.html') and not filename.endswith('.bak'):
                filepath = os.path.join(directory, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 1. Identify the preloader block (even if broken)
                # We look for the start <div id="preloader"> and the unique content inside
                # We replace everything from the start of the preloader until the next major section
                # OR until we find the closing sequence we expect.
                
                # First, try to find the whole block including potential orphans
                # This regex looks for the preloader and up to one extra closing div
                pattern = r'<div id="preloader">.*?VIJAYALAKSHMI GROUP.*?</div>\s*</div>(\s*</div>)?'
                
                if re.search(pattern, content, flags=re.DOTALL):
                    content = re.sub(pattern, new_html, content, flags=re.DOTALL)
                else:
                    # If the above didn't match, maybe it's the old ctn-preloader one
                    old_pattern = r'<div id="preloader">.*?id="ctn-preloader".*?</div>\s*</div>(\s*</div>)?'
                    content = re.sub(old_pattern, new_html, content, flags=re.DOTALL)

                # 2. Ensure main-page-wrapper is NOT closed prematurely
                # If we accidentally deleted a </div> that belonged to main-page-wrapper,
                # we need to make sure the header still comes after.
                # In the previous view, it looked like:
                # </div> <!-- end of preloader-content -->
                # [missing #preloader end]
                # <!-- Theme Main Menu -->
                
                # Let's check if the header is immediately preceded by the preloader
                # and ensure there are exactly two closing divs before the header.
                
                # Find the end of the preloader and the start of the next section
                # If there's only one </div> before "Theme Main Menu", add one.
                header_pattern = r'(<div id="preloader">.*?</div>)\s*(?=<!--\s*==+\s*Theme Main Menu|<header)'
                # This matches a preloader block that has only ONE trailing </div>
                if re.search(header_pattern, content, flags=re.DOTALL):
                    content = re.sub(header_pattern, r'\1\n\t\t</div>', content, flags=re.DOTALL)

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Fixed {filename}")

if __name__ == "__main__":
    fix_preloader_mess()
