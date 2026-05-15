import os

NEW_FOOTER = """
<footer class="footer-vjs-premium">
				<div class="footer-gold-bar"></div>
				<div class="footer-container">
					<div class="footer-main">
						<!-- Brand Column -->
						<div class="footer-column footer-brand-col">
							<div class="footer-logo">
								<div class="logo-icon-circle">
									<img src="/static/images/logo/vijayalakshmi-mark.png" alt="VJS Logo" style="width: 100%; height: 100%; object-fit: contain; border-radius: 50%;">
								</div>
								<div class="logo-text">
									<span class="brand-name">VIJAYALAKSHMI GROUP</span>
									<span class="brand-sub">OF COMPANIES</span>
								</div>
							</div>
							<div class="footer-divider-h"></div>
							<p class="brand-desc">Building legacies through vision, integrity, and excellence since decades.</p>
							<div class="social-links">
								<a href="#" class="social-box"><i class="bi bi-facebook"></i></a>
								<a href="#" class="social-box"><i class="bi bi-instagram"></i></a>
								<a href="#" class="social-box"><i class="bi bi-youtube"></i></a>
								<a href="#" class="social-box"><i class="bi bi-linkedin"></i></a>
							</div>
						</div>

						<!-- About Us Column -->
						<div class="footer-column">
							<h5 class="footer-title">ABOUT US</h5>
							<div class="title-underline"></div>
							<ul class="footer-links">
								<li><a href="/about-us-v2">About Company</a></li>
								<li><a href="/about-us-v1">Chairman's Office</a></li>
								<li><a href="/service-v1">Leadership</a></li>
								<li><a href="/about-us-v1">Our Journey</a></li>
								<li><a href="/service-v1">Awards</a></li>
							</ul>
						</div>

						<!-- Businesses Column -->
						<div class="footer-column">
							<h5 class="footer-title">BUSINESSES</h5>
							<div class="title-underline"></div>
							<ul class="footer-links">
								<li><a href="/it-consulting">Infrastructure</a></li>
								<li><a href="/green-energy">Energy & Utilities</a></li>
								<li><a href="/logistics-services">Transport & Logistics</a></li>
								<li><a href="/export-import">Consumer Products</a></li>
								<li><a href="/property-services">Real Estate</a></li>
								<li><a href="/yoga-wellness">Healthcare</a></li>
							</ul>
						</div>

						<!-- Quick Links Column -->
						<div class="footer-column">
							<h5 class="footer-title">QUICK LINKS</h5>
							<div class="title-underline"></div>
							<ul class="footer-links">
								<li><a href="/sustainability">Sustainability</a></li>
								<li><a href="/pricing">Investors</a></li>
								<li><a href="/media-release">Newsroom</a></li>
								<li><a href="/about-us-v1">Careers</a></li>
								<li><a href="/contact">Contact Us</a></li>
							</ul>
						</div>
					</div>
				</div>

				<!-- Bottom Bar -->
				<div class="footer-bottom-vjs">
					<div class="footer-container">
						<div class="bottom-inner">
							<div class="copyright">
								<i class="bi bi-crown-fill gold-icon"></i>
								<span>© 2026 Vijayalakshmi Group of Companies</span>
							</div>
							<div class="legal-links">
								<a href="#">All rights reserved</a>
                                <a href="/contact">Legal Disclaimer</a>
								<a href="/contact">Privacy Notice</a>
								<a href="/contact">Terms & Conditions</a>
								<a href="/contact">Cookie Policy</a>
							</div>
						</div>
					</div>
				</div>
			</footer>
"""

def safe_footer_sync(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html') and file != 'index-2.html.bak':
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 1. Remove existing footer-vjs-premium to avoid duplication
                if '<footer class="footer-vjs-premium">' in content:
                    import re
                    content = re.sub(r'<footer class="footer-vjs-premium">.*?</footer>', '', content, flags=re.DOTALL)

                # 2. Find and remove footer-modern block
                if '<div class="footer-modern">' in content:
                    import re
                    content = re.sub(r'<div class="footer-modern">.*?</div>\s*<!--\s*/\.footer-modern\s*-->', '', content, flags=re.DOTALL)
                    content = re.sub(r'<div class="footer-modern">.*?</div>', '', content, flags=re.DOTALL)
                
                # 3. Find and remove footer-mini block
                if '<div class="footer-mini">' in content:
                    import re
                    content = re.sub(r'<div class="footer-mini">.*?</div>', '', content, flags=re.DOTALL)

                # 4. Insert new footer outside the main-page-wrapper
                wrapper_marker = '</div> <!-- /.main-page-wrapper -->'
                if wrapper_marker not in content:
                    wrapper_marker = '</div> <!-- main-page-wrapper -->'
                
                if wrapper_marker in content:
                    parts = content.split(wrapper_marker)
                    new_content = parts[0] + wrapper_marker + "\n\n" + NEW_FOOTER + parts[1]
                else:
                    # Fallback before </body>
                    if '</body>' in content:
                        new_content = content.replace('</body>', NEW_FOOTER + '\n</body>')
                    else:
                        print(f"Skipping {file} - no insertion point found")
                        continue

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Safe sync success in {file}")

if __name__ == "__main__":
    templates_dir = r'c:\Users\Admin\vjgc-final\vjs-website\templates'
    safe_footer_sync(templates_dir)
