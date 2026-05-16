import os
import re

def clean_fix():
    new_block = """		<div id="preloader">
			<div class="preloader-content">
				<div class="logo-container">
					<div class="pulse-ring"></div>
					<div class="pulse-ring"></div>
					<div class="pulse-ring"></div>
					<div class="logo-circle" style="width: 120px; height: 120px; padding: 14px; background: #fff; border-radius: 50%; display: flex; align-items: center; justify-content: center; border: 1px solid rgba(197, 160, 89, 0.2);">
						<img src="{{ url_for('static', filename='images/logo/vijayalakshmi-mark.png') }}?v=1.0" alt="VJS Logo" style="width: 100%; height: 100%; object-fit: contain;">
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

                # CRITICAL CLEANUP: Replace everything between Transition comment and Theme Menu comment
                # This is the most reliable way as these comments are unique markers.
                pattern = r'(<!--\s*Loading Transition\s*-->).*?(?=<!--\s*==+\s*Theme Main Menu|<header)'
                
                if re.search(pattern, content, flags=re.DOTALL | re.IGNORECASE):
                    content = re.sub(pattern, rf'\1\n{new_block}\n\n\n\t\t', content, flags=re.DOTALL | re.IGNORECASE)
                    
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Cleaned {filename}")

if __name__ == "__main__":
    clean_fix()
