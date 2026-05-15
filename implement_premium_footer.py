import os
import glob
import re

css_path = 'static/css/custom.css'
templates_dir = 'templates'

premium_css = """
/* ==============================================
   PREMIUM DARK FOOTER STYLES
   ============================================== */
.footer-vjs-premium {
  background-color: #0b1120;
  color: #ffffff;
  position: relative;
  overflow: hidden;
  font-family: 'Plus Jakarta Sans', sans-serif;
  margin-top: 0;
}

.footer-gold-bar {
  height: 3px;
  background: linear-gradient(90deg, #b8860b 0%, #ffd700 50%, #b8860b 100%);
  width: 100%;
}

.footer-vjs-premium .footer-container {
  max-width: 1300px;
  margin: 0 auto;
  padding: 70px 40px;
}

.footer-main {
  display: grid;
  grid-template-columns: 1.5fr 1fr 1.2fr 1fr;
  gap: 30px;
}

.footer-column {
  position: relative;
  padding-left: 35px;
  border-left: 1px solid rgba(255, 255, 255, 0.08);
}

.footer-column:first-child {
  border-left: none;
  padding-left: 0;
}

/* Brand Section */
.footer-brand-col .footer-logo {
  display: flex;
  align-items: center;
  gap: 15px;
  margin-bottom: 25px;
}

.logo-icon-circle {
  width: 54px;
  height: 54px;
  border: 1.5px solid #d4af37;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #d4af37;
  font-size: 24px;
  background: rgba(212, 175, 55, 0.05);
}

.logo-text {
  display: flex;
  flex-direction: column;
}

.brand-name {
  font-size: 18px;
  font-weight: 800;
  letter-spacing: 1.5px;
  color: #ffffff;
  line-height: 1.2;
}

.brand-sub {
  font-size: 11px;
  letter-spacing: 3px;
  color: #d4af37;
  font-weight: 600;
}

.footer-divider-h {
  width: 60px;
  height: 2px;
  background: linear-gradient(90deg, #d4af37, transparent);
  margin-bottom: 25px;
}

.brand-desc {
  font-size: 15px;
  line-height: 1.7;
  color: rgba(255, 255, 255, 0.7);
  margin-bottom: 35px;
  font-weight: 400;
  max-width: 300px;
  font-style: italic;
}

.social-links {
  display: flex;
  gap: 12px;
}

.social-box {
  width: 38px;
  height: 38px;
  border: 1px solid rgba(212, 175, 55, 0.3);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #d4af37;
  border-radius: 6px;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  background: rgba(212, 175, 55, 0.03);
  text-decoration: none;
}

.social-box:hover {
  background: #d4af37;
  color: #0b1120 !important;
  box-shadow: 0 8px 20px rgba(212, 175, 55, 0.3);
  transform: translateY(-5px);
  border-color: #d4af37;
}

/* Titles */
.footer-title {
  color: #d4af37;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 2.5px;
  margin-bottom: 12px;
  text-transform: uppercase;
}

.title-underline {
  width: 35px;
  height: 2px;
  background: #d4af37;
  margin-bottom: 30px;
}

/* Links */
.footer-links {
  list-style: none;
  padding: 0;
  margin: 0;
}

.footer-links li {
  margin-bottom: 15px;
  position: relative;
  padding-left: 20px;
}

.footer-links li::before {
  content: "";
  position: absolute;
  left: 0;
  top: 50%;
  transform: translateY(-50%);
  width: 5px;
  height: 5px;
  background: rgba(212, 175, 55, 0.4);
  border-radius: 50%;
  transition: all 0.3s ease;
}

.footer-links li:hover::before {
  background: #d4af37;
  box-shadow: 0 0 10px #d4af37, 0 0 20px rgba(212, 175, 55, 0.6);
  transform: translateY(-50%) scale(1.3);
}

.footer-links li a {
  color: #a0aab2;
  text-decoration: none;
  font-size: 14.5px;
  transition: all 0.3s ease;
  font-weight: 400;
  display: inline-block;
}

.footer-links li a:hover {
  color: #d4af37;
  transform: translateX(5px);
}

/* Bottom Bar */
.footer-bottom-vjs {
  background: #070c17;
  padding: 25px 0;
  border-top: 1px solid rgba(255, 255, 255, 0.05);
}

.footer-bottom-vjs .footer-container {
  padding: 0 40px !important;
}

.bottom-inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.copyright {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 13px;
  color: rgba(255, 255, 255, 0.5);
  font-weight: 500;
}

.gold-icon {
  color: #d4af37;
  font-size: 16px;
}

.legal-links {
  display: flex;
  gap: 30px;
}

.legal-links a {
  color: rgba(255, 255, 255, 0.5);
  font-size: 13px;
  text-decoration: none;
  transition: all 0.3s ease;
  font-weight: 500;
}

.legal-links a:hover {
  color: #d4af37;
}

.scroll-top-wrap {
  display: flex;
  align-items: center;
}

.scroll-top-circle {
  width: 44px;
  height: 44px;
  border: 1px solid rgba(212, 175, 55, 0.3);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #d4af37;
  text-decoration: none;
  transition: all 0.4s ease;
  background: rgba(212, 175, 55, 0.05);
}

.scroll-top-circle:hover {
  background: #d4af37;
  color: #0b1120 !important;
  box-shadow: 0 0 20px rgba(212, 175, 55, 0.4);
  transform: translateY(-5px);
  border-color: #d4af37;
}

@media (max-width: 1024px) {
  .footer-main {
    grid-template-columns: 1fr 1fr;
    gap: 50px;
  }
  .footer-column {
    border-left: none;
    padding-left: 0;
  }
}

@media (max-width: 768px) {
  .bottom-inner {
    flex-direction: column;
    gap: 25px;
    text-align: center;
  }
  .legal-links {
    flex-wrap: wrap;
    justify-content: center;
    gap: 15px 25px;
  }
}

@media (max-width: 576px) {
  .footer-main {
    grid-template-columns: 1fr;
  }
  .footer-vjs-premium .footer-container {
    padding: 60px 25px;
  }
  .bottom-inner {
    text-align: center;
  }
}
"""

premium_html = """<!-- Footer -->
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
								<li><a href="{{ url_for('dynamic_route', path='about-us-v1') }}">Chairman's Office</a></li>
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
								<li><a href="{{ url_for('dynamic_route', path='yoga-wellness') }}">Healthcare</a></li>
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
								<span>© 2026 Vijayalakshmi Group of Companies</span>
							</div>
							<div class="legal-links">
								<a href="#">All rights reserved</a>
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

def do_dry_run():
    files_to_modify = []
    for filepath in glob.glob(f'{templates_dir}/**/*.html', recursive=True):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            if '<footer' in content or 'theme-footer' in content or 'footer-style' in content or 'footer-one' in content:
                files_to_modify.append(filepath)
    return files_to_modify

def append_css():
    with open(css_path, 'r', encoding='utf-8') as f:
        content = f.read()
    if '.footer-vjs-premium' not in content:
        with open(css_path, 'a', encoding='utf-8') as f:
            f.write('\\n' + premium_css)
        print("-> Injected Premium CSS into custom.css")

def replace_html(files_to_modify):
    for filepath in files_to_modify:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = re.sub(
            r'<!--\s*=+\s*Footer.*?(?:<footer|<div class="theme-footer|<div class="footer-style).*?(?:</footer>|</div>\s*<!--\s*/\.theme-footer\s*-->|</div>\s*<!--\s*/\.footer-style\s*-->)',
            premium_html,
            content,
            flags=re.DOTALL | re.IGNORECASE
        )
        
        if new_content == content:
            new_content = re.sub(r'<footer[^>]*>.*?</footer>', premium_html, content, flags=re.DOTALL | re.IGNORECASE)

        new_content = re.sub(r"custom\.css'\)\s*\}\}(?:\?v=[\d\.]+)?", r"custom.css') }}?v=3.0", new_content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
    print(f"-> HTML replacement and cache-busting (?v=3.0) applied to {len(files_to_modify)} templates.")

if __name__ == '__main__':
    print("=== DRY RUN ===")
    files = do_dry_run()
    print(f"Templates to be modified ({len(files)} files):")
    for file in files:
        print(f" - {file}")
    
    print("\\n=== PROCEEDING WITH MODIFICATIONS ===")
    append_css()
    replace_html(files)
    print("Done.")
