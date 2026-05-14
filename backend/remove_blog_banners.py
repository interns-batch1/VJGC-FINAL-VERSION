import os
import re

template_dir = r"C:\Users\ELCOT\vjs\vjs-website-\templates"

# Pattern 1: Fancy Banner Three
fancy_pattern = re.compile(r'<!--\s*=====================================================\s*Fancy Banner Three.*?<!-- /.fancy-banner-three -->', re.DOTALL)

# Pattern 2: Newsletter Banner
newsletter_pattern = re.compile(r'<!--\s*=====================================================\s*Newsletter Banner.*?<div class="newsletter-banner">.*?</div>\s*</div>\s*</div>', re.DOTALL)
# Improved Newsletter Pattern based on blog-details structure
newsletter_pattern_alt = re.compile(r'<!--\s*=====================================================\s*Newsletter Banner.*?<div class="newsletter-banner">.*?</div>\s*<!--\s*=====================================================', re.DOTALL)

# Target files
blog_files = ["blog-details.html", "blog-v1.html", "media-release.html", "media-kit.html"]

for filename in blog_files:
    path = os.path.join(template_dir, filename)
    if not os.path.exists(path): continue
    
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Remove Fancy Banner Three
    new_content = fancy_pattern.sub("", content)
    
    # Remove Newsletter Banner (try multiple patterns if needed)
    # We look for the start comment and go until the next major comment or the footer
    final_content = re.sub(r'<!--\s*=====================================================\s*Newsletter Banner.*?<!--\s*=====================================================\s*Footer', '', new_content, flags=re.DOTALL)
    
    # Fallback: if footer not found, just remove until the div ends
    if final_content == new_content:
         final_content = re.sub(r'<!--\s*=====================================================\s*Newsletter Banner.*?<div class="newsletter-banner">.*?</div>\s*</div>\s*</div>', '', new_content, flags=re.DOTALL)

    with open(path, "w", encoding="utf-8") as f:
        f.write(final_content)
    print(f"Removed banners from {filename}")

print("Blog banner removal complete.")
