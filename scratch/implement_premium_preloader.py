import os
import re

def implement_premium_preloader():
    # Define the new CSS
    new_css = """
		/* ===== PREMIUM BRANDED PRELOADER ===== */
		#preloader {
			position: fixed;
			inset: 0;
			z-index: 9999999;
			display: flex;
			align-items: center;
			justify-content: center;
			background: #ffffff;
			transition: opacity 0.8s cubic-bezier(0.4, 0, 0.2, 1), visibility 0.8s;
		}

		.preloader-content {
			text-align: center;
			display: flex;
			flex-direction: column;
			align-items: center;
			width: 100%;
			padding: 20px;
		}

		.logo-container {
			position: relative;
			width: 140px;
			height: 140px;
			margin-bottom: 40px;
			display: flex;
			align-items: center;
			justify-content: center;
		}

		.logo-circle {
			width: 120px;
			height: 120px;
			border: 1px solid rgba(197, 160, 89, 0.2);
			border-radius: 50%;
			padding: 14px;
			background: #fff;
			z-index: 5;
			display: flex;
			align-items: center;
			justify-content: center;
			animation: logoBreathing 4s ease-in-out infinite;
			box-shadow: 0 10px 30px rgba(0,0,0,0.03);
		}

		.logo-circle img {
			width: 100%;
			height: 100%;
			object-fit: contain;
		}

		.pulse-ring {
			position: absolute;
			width: 100px;
			height: 100px;
			border: 1.5px solid rgba(220, 38, 38, 0.25);
			border-radius: 50%;
			animation: ringPulse 4s cubic-bezier(0.25, 0.46, 0.45, 0.94) infinite;
			opacity: 0;
			z-index: 1;
		}

		.pulse-ring:nth-child(1) { animation-delay: 0s; }
		.pulse-ring:nth-child(2) { animation-delay: 1.3s; }
		.pulse-ring:nth-child(3) { animation-delay: 2.6s; }

		@keyframes ringPulse {
			0% { transform: scale(1); opacity: 0; }
			30% { opacity: 0.6; }
			100% { transform: scale(2.8); opacity: 0; }
		}

		@keyframes logoBreathing {
			0%, 100% { opacity: 1; transform: scale(1); }
			50% { opacity: 0.8; transform: scale(0.96); }
		}

		.brand-text {
			margin-bottom: 30px;
			opacity: 0;
			animation: fadeInText 1s ease-out 0.5s forwards;
		}

		.brand-main {
			color: #c5a059;
			font-size: 22px;
			font-weight: 700;
			letter-spacing: 8px;
			margin-bottom: 8px;
			text-transform: uppercase;
			font-family: 'Inter', sans-serif;
		}

		.brand-sub {
			color: #c5a059;
			font-size: 11px;
			font-weight: 500;
			letter-spacing: 4px;
			text-transform: uppercase;
			opacity: 0.8;
		}

		.loading-bar-container {
			width: 220px;
			height: 1px;
			background: rgba(197, 160, 89, 0.15);
			margin-bottom: 15px;
			position: relative;
			overflow: hidden;
		}

		.loading-bar-fill {
			position: absolute;
			top: 0;
			left: 0;
			height: 100%;
			background: #c5a059;
			width: 0%;
			animation: fillBar 4s cubic-bezier(0.65, 0, 0.35, 1) forwards;
		}

		@keyframes fillBar {
			0% { width: 0%; }
			100% { width: 100%; }
		}

		@keyframes fadeInText {
			from { opacity: 0; transform: translateY(10px); }
			to { opacity: 1; transform: translateY(0); }
		}

		.loading-text {
			color: #c5a059;
			font-size: 9px;
			letter-spacing: 5px;
			text-transform: uppercase;
			font-weight: 600;
			animation: blinkText 2.5s ease-in-out infinite;
			opacity: 0.7;
		}

		@keyframes blinkText {
			0%, 100% { opacity: 0.8; }
			50% { opacity: 0.2; }
		}"""

    new_html_template = """		<div id="preloader">
			<div class="preloader-content">
				<div class="logo-container">
					<div class="pulse-ring"></div>
					<div class="pulse-ring"></div>
					<div class="pulse-ring"></div>
					<div class="logo-circle">
						<img src="{logo_path}" alt="VJS Logo">
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

                # 1. Update/Inject CSS
                if 'PREMIUM BRANDED PRELOADER' in content:
                    # Already updated, refine if needed (handled by first script mostly)
                    pass
                else:
                    # Look for old CSS block
                    css_pattern_old = r'/\* ===== PRELOADER: Small \+ Centered ===== \*/.*?#preloader\s*\{.*?\}\s*#ctn-preloader\s*\{.*?\}\s*#ctn-preloader \.icon\s*\{.*?\}\s*\.site-loader-video\s*\{.*?\}'
                    if re.search(css_pattern_old, content, flags=re.DOTALL):
                        content = re.sub(css_pattern_old, new_css, content, flags=re.DOTALL)
                    else:
                        # Missing entirely, inject before </head>
                        content = content.replace('</head>', f'<style>{new_css}\n\t</style>\n</head>')

                # 2. Update/Inject HTML
                logo_path = "{{ url_for('static', filename='images/logo/vijayalakshmi-mark.png') }}?v=1.0"
                new_html = new_html_template.format(logo_path=logo_path)
                
                # Check for existing preloader div
                if '<div id="preloader">' in content:
                    # Replace old or already updated one
                    # Old one had ctn-preloader
                    if 'id="ctn-preloader"' in content:
                        html_pattern_old = r'<div id="preloader">.*?<div id="ctn-preloader".*?</div>\s*</div>'
                        # This was the bug: didn't include outer div end. Fixed:
                        html_pattern_old_fixed = r'<div id="preloader">.*?<div id="ctn-preloader".*?</div>\s*</div>'
                        # Let's try to match the whole block including the last </div>
                        # We know the old structure had 3 levels of nesting at most.
                        # Actually, let's just match until the next comment or header
                        html_pattern_aggressive = r'<div id="preloader">.*?</div>\s*</div>\s*(?=<!--|</div>|</body>)'
                        # Wait, that's dangerous.
                        # Let's just find the start and end of the block.
                        match = re.search(r'<div id="preloader">', content)
                        if match:
                            start = match.start()
                            # Count braces is hard for HTML.
                            # We'll just replace the whole block until we hit the next major comment
                            # which was "Theme Main Menu" or similar.
                            end_match = re.search(r'<!--\s*==+\s*Theme Main Menu', content)
                            if not end_match:
                                end_match = re.search(r'<header', content)
                            
                            if end_match:
                                end = end_match.start()
                                content = content[:start] + new_html + "\n\n\n" + content[end:]
                    else:
                        # Already updated, but check for orphaned divs
                        pattern_orphan = r'(<div id="preloader">.*?</div>\s*</div>)\s*</div>'
                        content = re.sub(pattern_orphan, r'\1', content, flags=re.DOTALL)
                else:
                    # Missing HTML? Inject at start of body
                    content = content.replace('<body>', f'<body>\n\t<div class="main-page-wrapper">\n{new_html}')

                # 3. Script injection (idempotent)
                if '<script id="vjs-preloader-script">' not in content:
                    vanilla_script = """
		<script id="vjs-preloader-script">
			window.addEventListener('load', function() {
				const preloader = document.getElementById('preloader');
				if (preloader) {
					preloader.style.opacity = '0';
					preloader.style.visibility = 'hidden';
					setTimeout(() => {
						preloader.style.display = 'none';
					}, 1000);
				}
				document.body.style.overflow = 'visible';
			});
		</script>"""
                    content = content.replace('</body>', vanilla_script + '\n</body>')

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Global Update: {filename}")

if __name__ == "__main__":
    implement_premium_preloader()
