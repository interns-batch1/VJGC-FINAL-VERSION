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

inline_styles = """
	<style>
		/* OVERRIDE FOR SCROLL TO TOP */
		#vjs-scroll-top.vjs-scroll-top-btn {
			position: fixed !important;
			bottom: 30px !important;
			right: 30px !important;
			width: 60px !important;
			height: 60px !important;
			background: linear-gradient(135deg, #A2D732 0%, #1A4137 100%) !important;
			border: none !important;
			border-radius: 50% !important;
			color: white !important;
			font-size: 24px !important;
			display: flex !important;
			align-items: center !important;
			justify-content: center !important;
			cursor: pointer !important;
			z-index: 100000 !important;
			opacity: 0 !important;
			visibility: hidden !important;
			transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
			box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3) !important;
			transform: translateY(20px) !important;
		}

		#vjs-scroll-top.vjs-scroll-top-btn.visible {
			opacity: 1 !important;
			visibility: visible !important;
			transform: translateY(0) !important;
		}

		#vjs-scroll-top.vjs-scroll-top-btn:hover {
			transform: translateY(-5px) scale(1.05) !important;
			box-shadow: 0 15px 40px rgba(162, 215, 50, 0.4) !important;
		}

		@media (max-width: 768px) {
			#vjs-scroll-top.vjs-scroll-top-btn {
				width: 50px !important;
				height: 50px !important;
				bottom: 20px !important;
				right: 20px !important;
				font-size: 20px !important;
			}
		}
	</style>
"""

scroll_top_html = """
	<!-- Standardized Scroll to Top Button -->
	<button id="vjs-scroll-top" class="vjs-scroll-top-btn" aria-label="Scroll to top">
		<i class="bi bi-chevron-double-up"></i>
	</button>

	<script>
		(function() {
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

			window.addEventListener('scroll', toggleScrollBtn, { passive: true });
			document.addEventListener('scroll', toggleScrollBtn, { passive: true });
			toggleScrollBtn();

			scrollTopBtn.addEventListener('click', function () {
				window.scrollTo({ top: 0, behavior: 'smooth' });
				document.documentElement.scrollTop = 0;
				document.body.scrollTop = 0;
			});
		})();
	</script>
"""

# Patterns to remove existing code
old_block_pattern = re.compile(r'<!-- Standardized Scroll to Top Button -->.*?<button id="vjs-scroll-top".*?</button>.*?<script>.*?</script>', re.DOTALL)
old_style_pattern = re.compile(r'<style>\s*/\* OVERRIDE FOR SCROLL TO TOP \*/.*?</style>', re.DOTALL)
old_v1_button = re.compile(r'<button id="vjs-scroll-top".*?</button>', re.DOTALL)
old_v1_script = re.compile(r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\', function \(\) \{.*?vjs-scroll-top.*?</script>', re.DOTALL)

for filepath in files_to_fix:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove any existing versions
        content = old_block_pattern.sub('', content)
        content = old_style_pattern.sub('', content)
        content = old_v1_button.sub('', content)
        content = old_v1_script.sub('', content)
        
        # Insert styles in head
        if '</head>' in content:
            content = content.replace('</head>', inline_styles + '\n</head>')
        
        # Insert button/script before </body>
        if '</body>' in content:
            content = content.replace('</body>', scroll_top_html + '\n</body>')
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Hard-fixed {filepath}")
    except Exception as e:
        print(f"Error hard-fixing {filepath}: {e}")
