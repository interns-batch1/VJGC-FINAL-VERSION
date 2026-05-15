import os
import re

# The new Premium White Card HTML structure for Jinja
NEW_CARD_JINJA = """
						<div class="col-lg-4 col-md-6 d-flex wow fadeInUp" data-wow-delay="{{ loop.index0 * 0.1 }}s">
							<div class="vjs-card-premium-white">
								<div class="card-img-box">
									<img src="{{ card.image_url if card.image_url else 'https://images.unsplash.com/photo-1451187534963-11d967f98ad4?auto=format&fit=crop&q=80&w=800' }}" alt="{{ card.title }}">
									<div class="card-badge-frosted">{category}</div>
								</div>
								<div class="card-content-area">
									<div class="card-header-row">
										<div class="card-icon-box"><i class="bi {icon_class}"></i></div>
										<div class="card-header-divider"></div>
									</div>
									<h4 class="serif-heading">{{ card.title }}</h4>
									<p class="muted-desc">{{ card.description }}</p>
									<div class="card-footer-divider"></div>
									<a href="#" class="discover-more-link">
										DISCOVER MORE <i class="bi bi-arrow-right"></i>
									</a>
								</div>
							</div>
						</div>"""

# The new Premium White Card HTML structure for Static Fallback
NEW_CARD_STATIC = """
						<div class="col-lg-4 col-md-6 d-flex wow fadeInUp" {delay_attr}>
							<div class="vjs-card-premium-white">
								<div class="card-img-box">
									<img src="{image_url}" alt="{heading}">
									<div class="card-badge-frosted">{category}</div>
								</div>
								<div class="card-content-area">
									<div class="card-header-row">
										<div class="card-icon-box"><i class="bi {icon_class}"></i></div>
										<div class="card-header-divider"></div>
									</div>
									<h4 class="serif-heading">{heading}</h4>
									<p class="muted-desc">{description}</p>
									<div class="card-footer-divider"></div>
									<a href="#" class="discover-more-link">
										DISCOVER MORE <i class="bi bi-arrow-right"></i>
									</a>
								</div>
							</div>
						</div>"""

def sync_premium_cards(directory):
    page_icons = {
        'it-consulting': 'bi-cpu',
        'green-energy': 'bi-sun',
        'logistics-services': 'bi-truck',
        'export-import': 'bi-globe-americas',
        'property-services': 'bi-building',
        'yoga-wellness': 'bi-heart-pulse',
        'travel-rentals': 'bi-airplane',
        'data-centers-hosting': 'bi-server'
    }

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html') and file != 'index-2.html':
                file_path = os.path.join(root, file)
                page_key = file.replace('.html', '')
                icon = page_icons.get(page_key, 'bi-briefcase')
                category = page_key.replace('-', ' ').upper()
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 1. Replace Jinja Card
                jinja_pattern = re.compile(r'<div class="col-lg-3 col-md-6 d-flex wow fadeInUp" data-wow-delay="{{ loop.index0 \* 0.1 }}s">.*?<div class="vjs-glance-card-v3">.*?</div>\s*</div>', re.DOTALL)
                new_content = jinja_pattern.sub(NEW_CARD_JINJA.replace('{category}', category).replace('{icon_class}', icon), content)

                # 2. Replace Static Fallback Cards
                static_pattern = re.compile(r'<div class="col-lg-3 col-md-6 d-flex wow fadeInUp"(?P<delay>.*?)>.*?<div class="vjs-glance-card-v3">.*?<img.*?src="(?P<img_url>.*?)".*?><h4 class="card-title">(?P<title>.*?)</h4>.*?<p class="card-desc">(?P<desc>.*?)</p>.*?</div>\s*</div>', re.DOTALL | re.IGNORECASE)
                
                def replace_static(match):
                    d = match.groupdict()
                    return NEW_CARD_STATIC.format(
                        delay_attr=d['delay'],
                        image_url=d['img_url'],
                        heading=d['title'],
                        category=category,
                        icon_class=icon,
                        description=d['desc']
                    )

                new_content = static_pattern.sub(replace_static, new_content)
                
                # 3. Update row class for featured effect (middle card elevation)
                new_content = new_content.replace('row justify-content-center g-4', 'row vjs-card-row justify-content-center g-4')

                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Successfully redesigned cards in {file}")

if __name__ == "__main__":
    templates_dir = r'c:\Users\Admin\vjgc-final\vjs-website\templates'
    sync_premium_cards(templates_dir)
