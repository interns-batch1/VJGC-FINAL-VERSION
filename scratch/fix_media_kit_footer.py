import os
import re

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

def fix_media_kit():
    file_path = r'c:\Users\Admin\vjgc-final\vjs-website\templates\media-kit.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove everything after the last section
    pattern = re.compile(r'<!-- Footer -->.*', re.DOTALL | re.IGNORECASE)
    new_content = pattern.sub('', content)
    
    # Add the new footer and correct closing tags
    final_content = new_content + "\n" + NEW_FOOTER + """
    </div> <!-- /.main-page-wrapper -->
    <script src="/static/vendor/jquery.min.js?v=1.0"></script>
	<script src="/static/vendor/bootstrap/js/bootstrap.bundle.min.js?v=1.0"></script>
	<script src="/static/js/theme.js?v=1.0"></script>
	<script src="/static/js/mega-dropdown.js?v=1.0"></script>
    </body>
</html>
"""
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_content)

if __name__ == "__main__":
    fix_media_kit()
