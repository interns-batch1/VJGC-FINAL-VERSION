import os
import re

# The new Premium White Card HTML structure
# We use placeholders for: IMAGE_URL, CATEGORY, ICON_CLASS, HEADING, DESCRIPTION, LINK_URL
NEW_CARD_HTML = """
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
                                    <a href="{link_url}" class="discover-more-link">
                                        DISCOVER MORE <i class="bi bi-arrow-right"></i>
                                    </a>
                                </div>
                            </div>
                        </div>"""

def sync_premium_cards(directory):
    # Regex to find the "At a Glance" or similar card sections
    # Specifically targeting the glance-section-v3 and its variants
    section_pattern = re.compile(r'<section class="(glance-section-v3|glance-section-v1|glance-section-v2)">.*?</section>', re.DOTALL | re.IGNORECASE)
    
    # Pattern to extract card data from the old vjs-glance-card-v3
    card_pattern = re.compile(r'<div class="vjs-glance-card-v3">.*?<img.*?src="(?P<img_url>.*?)".*?><h4 class="card-title">(?P<title>.*?)</h4>.*?<p class="card-desc">(?P<desc>.*?)</p>', re.DOTALL | re.IGNORECASE)
    
    # Icons for different pages
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
            if file.endswith('.html') and file != 'index-2.html': # DO NOT TOUCH HOME PAGE
                file_path = os.path.join(root, file)
                page_key = file.replace('.html', '')
                icon = page_icons.get(page_key, 'bi-briefcase')
                category = page_key.replace('-', ' ').upper()
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                def replace_section(match):
                    section_content = match.group(0)
                    # Extract cards
                    cards_data = []
                    for card_match in card_pattern.finditer(section_content):
                        cards_data.append(card_match.groupdict())
                    
                    if not cards_data:
                        return section_content # No cards found
                    
                    # Build new grid
                    new_grid_html = '<section class="vjs-premium-card-section py-5">\n    <div class="container">\n        <div class="row vjs-card-row g-4 justify-content-center">'
                    
                    for i, card in enumerate(cards_data):
                        delay = f'data-wow-delay="{0.1 * i}s"' if i > 0 else ''
                        new_grid_html += NEW_CARD_HTML.format(
                            delay_attr=delay,
                            image_url=card['img_url'],
                            heading=card['title'],
                            category=category,
                            icon_class=icon,
                            description=card['desc'],
                            link_url="#" # Link preserved or default
                        )
                    
                    new_grid_html += '\n        </div>\n    </div>\n</section>'
                    return new_grid_html

                new_content = section_pattern.sub(replace_section, content)
                
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Successfully redesigned cards in {file}")

if __name__ == "__main__":
    templates_dir = r'c:\Users\Admin\vjgc-final\vjs-website\templates'
    sync_premium_cards(templates_dir)
