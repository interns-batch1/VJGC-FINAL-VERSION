import os
import re

templates_dir = r"c:\Users\Admin\vjgc-final\vjs-website\templates"
sustainability_keywords = [
    "sustainability", "eco-tech", "renewable", "energy-adoption", 
    "sustainable-business", "educational-support-csr", "financial-material-aid",
    "skill-building-youth", "rural-semi-urban", "awareness-programs",
    "local-infrastructure-support", "digital-transformation", "cloud-infrastructure",
    "logistics-trade", "tree-plantation", "education-skill"
]

files_to_fix = []
for filename in os.listdir(templates_dir):
    if filename.endswith(".html"):
        if any(keyword in filename.lower() for keyword in sustainability_keywords):
            files_to_fix.append(os.path.join(templates_dir, filename))

if os.path.exists(os.path.join(templates_dir, "yoga-wellness.html")):
    files_to_fix.append(os.path.join(templates_dir, "yoga-wellness.html"))

scroll_top_html = """
	<!-- Standardized Scroll to Top Button -->
	<button id="vjs-scroll-top" class="vjs-scroll-top-btn" aria-label="Scroll to top">
		<i class="bi bi-chevron-double-up"></i>
	</button>

	<script>
		document.addEventListener('DOMContentLoaded', function () {
			const scrollTopBtn = document.getElementById('vjs-scroll-top');
			if (!scrollTopBtn) return;

			function toggleScrollBtn() {
				const scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0;
				if (scrollTop > 300) {
					scrollTopBtn.classList.add('visible');
				} else {
					scrollTopBtn.classList.remove('visible');
				}
			}

			// Listen to scroll on window and body
			window.addEventListener('scroll', toggleScrollBtn, { passive: true });
			document.addEventListener('scroll', toggleScrollBtn, { passive: true });
			
			// Initial check
			toggleScrollBtn();

			scrollTopBtn.addEventListener('click', function () {
				window.scrollTo({
					top: 0,
					behavior: 'smooth'
				});
				// Fallback for older browsers
				document.documentElement.scrollTop = 0;
				document.body.scrollTop = 0;
			});
		});
	</script>
"""

# Patterns to remove existing code
button_pattern = re.compile(r'<!-- Standardized Scroll to Top Button -->.*?<button id="vjs-scroll-top".*?</button>.*?<script>.*?</script>', re.DOTALL)
old_button_pattern = re.compile(r'<button id="vjs-scroll-top".*?</button>', re.DOTALL)
old_script_pattern = re.compile(r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\', function \(\) \{.*?vjs-scroll-top.*?</script>', re.DOTALL)

for filepath in files_to_fix:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove any existing versions (standardized or old)
        new_content = button_pattern.sub('', content)
        new_content = old_button_pattern.sub('', new_content)
        new_content = old_script_pattern.sub('', new_content)
        
        # Insert new button/script before </body>
        if '</body>' in new_content:
            new_content = new_content.replace('</body>', scroll_top_html + '\n</body>')
        else:
            new_content += scroll_top_html
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Enhanced {filepath}")
    except Exception as e:
        print(f"Error enhancing {filepath}: {e}")
