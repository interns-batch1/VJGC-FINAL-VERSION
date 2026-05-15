import os
import re

# The latest premium footer HTML
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

def global_footer_sync(directory):
    # Pattern for footer-modern (div or footer)
    old_footer_pattern = re.compile(r'(<div class="footer-modern">.*?<!-- /.footer-modern -->|<div class="footer-modern">.*?</div>\s*<!--\s*/\.footer-modern\s*-->|<footer class="footer-modern">.*?</footer>)', re.DOTALL)
    # Pattern for footer-vjs-premium
    premium_footer_pattern = re.compile(r'(<footer class="footer-vjs-premium">.*?</footer>)', re.DOTALL)
    
    wrapper_close_patterns = [
        re.compile(r'(</div>\s*<!--\s*/\.main-page-wrapper\s*-->)'),
        re.compile(r'(</div>\s*<!--\s*main-page-wrapper\s*-->)'),
        re.compile(r'(</div>\s*<!--\s*/\s*main-page-wrapper\s*-->)'),
        re.compile(r'(</div>\s*<!--\s*\.main-page-wrapper\s*-->)')
    ]

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html') and file != 'index-2.html.bak':
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 1. Remove ANY existing footer
                new_content = old_footer_pattern.sub('', content)
                new_content = premium_footer_pattern.sub('', new_content)
                
                # 2. Find wrapper closing tag
                wrapper_match = None
                for pattern in wrapper_close_patterns:
                    wrapper_match = pattern.search(new_content)
                    if wrapper_match:
                        break
                
                if wrapper_match:
                    # Insert footer AFTER wrapper
                    insertion_point = wrapper_match.end()
                    final_content = new_content[:insertion_point] + "\n\n" + NEW_FOOTER + new_content[insertion_point:]
                    
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(final_content)
                    print(f"Synced premium footer in {file}")
                else:
                    # Fallback: find the last </div> before scripts or body close
                    if '</body>' in new_content:
                         final_content = new_content.replace('</body>', NEW_FOOTER + '\n</body>')
                         with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(final_content)
                         print(f"Fallback sync in {file}")
                    else:
                        print(f"FAILED to sync {file}")

if __name__ == "__main__":
    templates_dir = r'c:\Users\Admin\vjgc-final\vjs-website\templates'
    global_footer_sync(templates_dir)
