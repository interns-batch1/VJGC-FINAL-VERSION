import os
import re

def final_template_repair(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html') and file != 'index-2.html':
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 1. Fix duplicated row classes
                new_content = re.sub(r'class="row (vjs-card-row\s*)+', 'class="row vjs-card-row ', content)
                
                # 2. Fix the dangling </div> and the empty src/desc
                # We'll just re-run the extraction with a better pattern and replace the whole block
                
                # Identify the "At a Glance" section
                section_pattern = re.compile(r'<section class="glance-section-v3">.*?</section>', re.DOTALL)
                
                def repair_section(match):
                    # For simplicity, we'll just restore it to a known good state with the new design
                    # Since I know the data structure, I can just hardcode the fallback and use Jinja for the rest
                    
                    page_key = file.replace('.html', '')
                    category = page_key.replace('-', ' ').upper()
                    icons = {
                        'it-consulting': 'bi-cpu',
                        'green-energy': 'bi-sun',
                        'logistics-services': 'bi-truck',
                        'export-import': 'bi-globe-americas',
                        'property-services': 'bi-building',
                        'yoga-wellness': 'bi-heart-pulse',
                        'travel-rentals': 'bi-airplane',
                        'data-centers-hosting': 'bi-server'
                    }
                    icon = icons.get(page_key, 'bi-briefcase')

                    # Extract the actual content if possible, otherwise use standard fallback
                    # This is just a repair script, so we'll be careful
                    
                    repaired_html = f"""
			<section class="glance-section-v3 py-5">
				<div class="container">
					<h2 class="section-title text-center mb-5">At a Glance.</h2>
					<div class="row vjs-card-row justify-content-center g-4">
						{{% if cms['At a Glance'] and cms['At a Glance'].content %}}
						{{% for card in cms['At a Glance'].content %}}
						<div class="col-lg-4 col-md-6 d-flex wow fadeInUp" data-wow-delay="{{{{ loop.index0 * 0.1 }}}}s">
							<div class="vjs-card-premium-white">
								<div class="card-img-box">
									<img src="{{{{ card.image_url if card.image_url else 'https://images.unsplash.com/photo-1451187534963-11d967f98ad4?auto=format&fit=crop&q=80&w=800' }}}}" alt="{{{{ card.title }}}}">
									<div class="card-badge-frosted">{category}</div>
								</div>
								<div class="card-content-area">
									<div class="card-header-row">
										<div class="card-icon-box"><i class="bi {icon}"></i></div>
										<div class="card-header-divider"></div>
									</div>
									<h4 class="serif-heading">{{{{ card.title }}}}</h4>
									<p class="muted-desc">{{{{ card.description }}}}</p>
									<div class="card-footer-divider"></div>
									<a href="#" class="discover-more-link">
										DISCOVER MORE <i class="bi bi-arrow-right"></i>
									</a>
								</div>
							</div>
						</div>
						{{% endfor %}}
						{{% else %}}
						<!-- Fallback Content -->
						<div class="col-lg-4 col-md-6 d-flex wow fadeInUp">
							<div class="vjs-card-premium-white">
								<div class="card-img-box">
									<img src="/static/images/media/vjs_{page_key}_glance_1.png" alt="Excellence">
									<div class="card-badge-frosted">{category}</div>
								</div>
								<div class="card-content-area">
									<div class="card-header-row">
										<div class="card-icon-box"><i class="bi {icon}"></i></div>
										<div class="card-header-divider"></div>
									</div>
									<h4 class="serif-heading">Strategic Excellence</h4>
									<p class="muted-desc">Driving value through innovation and industry-leading standards.</p>
									<div class="card-footer-divider"></div>
									<a href="#" class="discover-more-link">
										DISCOVER MORE <i class="bi bi-arrow-right"></i>
									</a>
								</div>
							</div>
						</div>
                        <div class="col-lg-4 col-md-6 d-flex wow fadeInUp" data-wow-delay="0.1s">
							<div class="vjs-card-premium-white">
								<div class="card-img-box">
									<img src="/static/images/media/vjs_{page_key}_glance_2.png" alt="Innovation">
									<div class="card-badge-frosted">{category}</div>
								</div>
								<div class="card-content-area">
									<div class="card-header-row">
										<div class="card-icon-box"><i class="bi {icon}"></i></div>
										<div class="card-header-divider"></div>
									</div>
									<h4 class="serif-heading">Global Innovation</h4>
									<p class="muted-desc">Transforming sectors with future-ready technology and expert insights.</p>
									<div class="card-footer-divider"></div>
									<a href="#" class="discover-more-link">
										DISCOVER MORE <i class="bi bi-arrow-right"></i>
									</a>
								</div>
							</div>
						</div>
						{{% endif %}}
					</div>
				</div>
			</section>"""
                    return repaired_html

                new_content = section_pattern.sub(repair_section, new_content)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Repaired {file}")

if __name__ == "__main__":
    final_template_repair(r'c:\Users\Admin\vjgc-final\vjs-website\templates')
