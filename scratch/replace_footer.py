import os
import re

# Define the new footer HTML
NEW_FOOTER = """
			<!-- Footer -->
			<footer class="footer-vjs-premium">
				<div class="footer-gold-bar"></div>
				<div class="footer-container">
					<div class="footer-main">
						<!-- Brand Column -->
						<div class="footer-column footer-brand-col">
							<div class="footer-logo">
								<div class="logo-icon-circle">
									<i class="bi bi-crown-fill"></i>
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
								<li><a href="{{ url_for('dynamic_route', path='about-us-v2') }}">About Company</a></li>
								<li><a href="{{ url_for('dynamic_route', path='about-us-v1') }}">Chairman’s Office</a></li>
								<li><a href="{{ url_for('dynamic_route', path='service-v1') }}">Leadership</a></li>
								<li><a href="{{ url_for('dynamic_route', path='about-us-v1') }}">Our Journey</a></li>
								<li><a href="{{ url_for('dynamic_route', path='service-v1') }}">Awards</a></li>
							</ul>
						</div>

						<!-- Businesses Column -->
						<div class="footer-column">
							<h5 class="footer-title">BUSINESSES</h5>
							<div class="title-underline"></div>
							<ul class="footer-links">
								<li><a href="{{ url_for('dynamic_route', path='it-consulting') }}">Infrastructure</a></li>
								<li><a href="{{ url_for('dynamic_route', path='green-energy') }}">Energy & Utilities</a></li>
								<li><a href="{{ url_for('dynamic_route', path='logistics-services') }}">Transport & Logistics</a></li>
								<li><a href="{{ url_for('dynamic_route', path='export-import') }}">Consumer Products</a></li>
								<li><a href="{{ url_for('dynamic_route', path='property-services') }}">Real Estate</a></li>
								<li><a href="{{ url_for('dynamic_route', path='healthcare') }}">Healthcare</a></li>
							</ul>
						</div>

						<!-- Quick Links Column -->
						<div class="footer-column">
							<h5 class="footer-title">QUICK LINKS</h5>
							<div class="title-underline"></div>
							<ul class="footer-links">
								<li><a href="{{ url_for('dynamic_route', path='sustainability') }}">Sustainability</a></li>
								<li><a href="{{ url_for('dynamic_route', path='pricing') }}">Investors</a></li>
								<li><a href="{{ url_for('dynamic_route', path='media-release') }}">Newsroom</a></li>
								<li><a href="{{ url_for('dynamic_route', path='about-us-v1') }}">Careers</a></li>
								<li><a href="{{ url_for('dynamic_route', path='contact') }}">Contact Us</a></li>
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
								<span>© 2026 Vijayalakshmi Group of Companies. All rights reserved.</span>
							</div>
							<div class="legal-links">
								<a href="{{ url_for('dynamic_route', path='contact') }}">Legal Disclaimer</a>
								<a href="{{ url_for('dynamic_route', path='contact') }}">Privacy Notice</a>
								<a href="{{ url_for('dynamic_route', path='contact') }}">Terms & Conditions</a>
								<a href="{{ url_for('dynamic_route', path='contact') }}">Cookie Policy</a>
							</div>
							<div class="scroll-top-wrap">
								<a href="#" class="scroll-top-circle"><i class="bi bi-arrow-up"></i></a>
							</div>
						</div>
					</div>
				</div>
			</footer>"""

# Regex to find the old footer block
FOOTER_RE = re.compile(r'<div class="footer-modern">.*?</div> <!-- /.footer-modern -->', re.DOTALL)

# Regex to find the old scroll-top button and its script
SCROLL_RE = re.compile(r'<button id="vjs-scroll-top".*?</script>', re.DOTALL)

TEMPLATE_DIR = r'c:\Users\Admin\vjgc-final\vjs-website\templates'

for filename in os.listdir(TEMPLATE_DIR):
    if filename.endswith('.html'):
        filepath = os.path.join(TEMPLATE_DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace footer
        new_content = FOOTER_RE.sub(NEW_FOOTER, content)
        
        # Also handle cases where there might be slight variations or missing comment
        if new_content == content:
             alt_footer_re = re.compile(r'<div class="footer-modern">.*?</div>\s*</div>\s*<!-- Optional JavaScript -->', re.DOTALL)
             # Wait, yoga-wellness.html has it inside another div maybe?
             # Let's check yoga-wellness lines 448-532.
             pass

        # Remove the old scroll top button and its script if present
        new_content = SCROLL_RE.sub('', new_content)

        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
        else:
            print(f"No changes for {filename}")
