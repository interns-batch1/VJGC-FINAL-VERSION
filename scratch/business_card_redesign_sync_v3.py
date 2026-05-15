import os
import re

# Template for the new card
NEW_CARD_TEMPLATE = """
                        <div class="col-lg-4 col-md-6 d-flex wow fadeInUp" {delay}>
                            <div class="vjs-card-premium-white">
                                <div class="card-img-box">
                                    <img src="{img_url}" alt="{title}">
                                    <div class="card-badge-frosted">{category}</div>
                                </div>
                                <div class="card-content-area">
                                    <div class="card-header-row">
                                        <div class="card-icon-box"><i class="bi {icon}"></i></div>
                                        <div class="card-header-divider"></div>
                                    </div>
                                    <h4 class="serif-heading">{title}</h4>
                                    <p class="muted-desc">{desc}</p>
                                    <div class="card-footer-divider"></div>
                                    <a href="#" class="discover-more-link">
                                        DISCOVER MORE <i class="bi bi-arrow-right"></i>
                                    </a>
                                </div>
                            </div>
                        </div>"""

def redesign_business_cards(directory):
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

                # Find all glance cards
                # We'll match the col-lg-3 block that contains vjs-glance-card-v3
                # This pattern is robust against whitespace
                pattern = re.compile(r'<div class="col-lg-3 col-md-6 d-flex wow fadeInUp".*?vjs-glance-card-v3.*?</div>\s*</div>', re.DOTALL)
                
                matches = list(pattern.finditer(content))
                if not matches:
                    continue

                new_content = content
                # Work backwards to avoid index shifts
                for match in reversed(matches):
                    block = match.group(0)
                    
                    # Extract delay
                    delay_match = re.search(r'data-wow-delay="(.*?)"', block)
                    delay = f'data-wow-delay="{delay_match.group(1)}"' if delay_match else ''
                    
                    # Extract image
                    img_match = re.search(r'<img.*?src="(.*?)"', block)
                    img_url = img_match.group(1) if img_match else ""
                    
                    # Extract title
                    title_match = re.search(r'<h4.*?>(.*?)</h4>', block)
                    title = title_match.group(1) if title_match else ""
                    
                    # Extract desc
                    desc_match = re.search(r'<p.*?>(.*?)</p>', block)
                    desc = desc_match.group(1) if desc_match else ""
                    
                    # Construct new card
                    new_card = NEW_CARD_TEMPLATE.format(
                        delay=delay,
                        img_url=img_url,
                        title=title,
                        category=category,
                        icon=icon,
                        desc=desc
                    )
                    
                    new_content = new_content[:match.start()] + new_card + new_content[match.end():]
                
                # Update row class
                new_content = new_content.replace('row justify-content-center g-4', 'row vjs-card-row justify-content-center g-4')
                
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Redesigned cards in {file}")

if __name__ == "__main__":
    redesign_business_cards(r'c:\Users\Admin\vjgc-final\vjs-website\templates')
