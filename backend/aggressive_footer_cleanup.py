import os
import re

template_dir = r"C:\Users\ELCOT\vjs\vjs-website-\templates"

standard_footer = '''			<div class="footer-modern">
				<div class="footer-container">
					<div class="footer-top">
						<!-- LOGO & BRAND -->
						<div class="footer-brand">
							<div class="footer-logo-group">
								<img src="{{ url_for(\'static\', filename=\'images/logo/vijayalakshmi-mark.png\') }}?v=1.0"
									alt="Logo Mark">
								<div class="footer-logo-text">
									<span>Vijayalakshmi Group</span>
									<span>OF COMPANIES</span>
								</div>
							</div>

							<div class="social-icons-mini">
								<a href="#"><i class="bi bi-facebook"></i></a>
								<a href="#"><i class="bi bi-instagram"></i></a>
								<a href="#"><i class="bi bi-youtube"></i></a>
								<a href="#"><i class="bi bi-linkedin"></i></a>
							</div>
						</div>

						<!-- ABOUT -->
						<div class="footer-col">
							<h5>About Us</h5>
							<ul>
								<li><a href="{{ url_for(\'dynamic_route\', path=\'about-us-v2\') }}">About Company</a></li>
								<li><a href="{{ url_for(\'dynamic_route\', path=\'about-us-v1\') }}">Chairman’s Office</a>
								</li>
								<li><a href="{{ url_for(\'dynamic_route\', path=\'service-v1\') }}">Leadership</a></li>
								<li><a href="{{ url_for(\'dynamic_route\', path=\'about-us-v1\') }}">Our Journey</a></li>
								<li><a href="{{ url_for(\'dynamic_route\', path=\'service-v1\') }}">Awards</a></li>
							</ul>
						</div>

						<!-- BUSINESS -->
						<div class="footer-col">
							<h5>Businesses</h5>
							<ul>
								<li><a href="{{ url_for(\'dynamic_route\', path=\'it-consulting\') }}">Infrastructure</a>
								</li>
								<li><a href="{{ url_for(\'dynamic_route\', path=\'green-energy\') }}">Energy & Utilities</a>
								</li>
								<li><a href="{{ url_for(\'dynamic_route\', path=\'logistics-services\') }}">Transport &
										Logistics</a></li>
								<li><a href="{{ url_for(\'dynamic_route\', path=\'export-import\') }}">Consumer Products</a>
								</li>
								<li><a href="{{ url_for(\'dynamic_route\', path=\'property-services\') }}">Real Estate</a>
								</li>
								<li><a href="{{ url_for(\'dynamic_route\', path=\'yoga-wellness\') }}">Healthcare</a></li>
							</ul>
						</div>

						<!-- QUICK LINKS -->
						<div class="footer-col">
							<h5>Quick Links</h5>
							<ul>
								<li><a
										href="{{ url_for(\'dynamic_route\', path=\'digital-transformation-sustainability\') }}">Sustainability</a>
								</li>
								<li><a href="{{ url_for(\'dynamic_route\', path=\'pricing\') }}">Investors</a></li>
								<li><a href="{{ url_for(\'dynamic_route\', path=\'media-release\') }}">Newsroom</a></li>
								<li><a href="{{ url_for(\'dynamic_route\', path=\'about-us-v1\') }}">Careers</a></li>
								<li><a href="{{ url_for(\'dynamic_route\', path=\'contact\') }}">Contact Us</a></li>
							</ul>
						</div>
					</div>

					<!-- BOTTOM -->
					<div class="footer-bottom">
						<div class="footer-copyright">
							<img src="{{ url_for(\'static\', filename=\'images/logo/vijayalakshmi-mark.png\') }}?v=1.0"
								alt="Mark">
							<span>@2026 Vijayalakshmi Group</span>
						</div>

						<div class="footer-bottom-links">
							<a href="{{ url_for(\'dynamic_route\', path=\'contact\') }}">Legal Disclaimer</a>
							<a href="{{ url_for(\'dynamic_route\', path=\'contact\') }}">Privacy Notice</a>
							<a href="{{ url_for(\'dynamic_route\', path=\'contact\') }}">Terms & Conditions</a>
							<a href="{{ url_for(\'dynamic_route\', path=\'contact\') }}">Cookie Policy</a>
						</div>
					</div>
				</div>
			</div> <!-- /.footer-modern -->'''

# Aggressive Regex: find from the VERY FIRST footer-modern to the VERY LAST footer-modern marker
# or until the wrapper div ends.
aggressive_pattern = re.compile(r'<div class="footer-modern">.*?</div> <!-- /.footer-modern -->(\s*<!-- ABOUT -->.*?</div> <!-- /.footer-modern -->)?', re.DOTALL)

for filename in os.listdir(template_dir):
    if filename.endswith(".html"):
        path = os.path.join(template_dir, filename)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        
        if "footer-modern" in content:
            # We first replace the full block including any "zombie" footers that followed
            # We do this by searching for the start and going until the last marker
            
            # Find all occurrences of the footer-modern end marker
            end_markers = [m.end() for m in re.finditer(r'</div> <!-- /.footer-modern -->', content)]
            if end_markers:
                first_start = content.find('<div class="footer-modern">')
                last_end = end_markers[-1]
                
                if first_start != -1:
                    new_content = content[:first_start] + standard_footer + content[last_end:]
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Cleaned and standardized footer in {filename}")

print("Aggressive global footer cleanup complete.")
