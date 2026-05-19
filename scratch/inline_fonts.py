import os
import re
import subprocess

static_dir = r"c:\Users\Admin\vjgc-final\vjs-website\static"

# Reset style.min.css to the git version first to avoid duplicates
style_min_path = os.path.join(static_dir, "css", "style.min.css")
print("Resetting style.min.css to clean git status...")
subprocess.run(["git", "checkout", "--", style_min_path], check=True)

# 1. Satoshi
satoshi_path = os.path.join(static_dir, "fonts", "Satoshi", "css", "satoshi.css")
with open(satoshi_path, "r", encoding="utf-8-sig") as f:
    satoshi_css = f.read()
# Replace relative paths
satoshi_css = satoshi_css.replace("../fonts/", "../fonts/Satoshi/fonts/")

# 2. ClashDisplay
clash_path = os.path.join(static_dir, "fonts", "ClashDisplay", "css", "clash-display.css")
with open(clash_path, "r", encoding="utf-8-sig") as f:
    clash_css = f.read()
# Replace relative paths
clash_css = clash_css.replace("../fonts/", "../fonts/ClashDisplay/fonts/")

# 3. Magnita
magnita_path = os.path.join(static_dir, "fonts", "Magnita", "Magnita.css")
with open(magnita_path, "r", encoding="utf-8-sig") as f:
    magnita_css = f.read()
# Replace relative paths
magnita_css = magnita_css.replace("fonts/", "../fonts/Magnita/fonts/")

# 4. Bootstrap Icons
bi_path = os.path.join(static_dir, "fonts", "bootstrap-icons-1.10.2", "font.css")
with open(bi_path, "r", encoding="utf-8-sig") as f:
    bi_css = f.read()
# Replace relative paths
bi_css = bi_css.replace('url("', 'url("../fonts/bootstrap-icons-1.10.2/')

# Minify helpers
def minify_css(css):
    # Remove comments
    css = re.sub(r'/\*[\s\S]*?\*/', '', css)
    # Remove whitespace
    css = re.sub(r'\s+', ' ', css)
    css = re.sub(r'\s*([\{\}:;\,])\s*', r'\1', css)
    return css.strip()

inlined_css = (
    minify_css(satoshi_css) +
    minify_css(clash_css) +
    minify_css(magnita_css) +
    minify_css(bi_css)
)

# Strip any residual BOM character
inlined_css = inlined_css.replace('\ufeff', '')

# Load current style.min.css
with open(style_min_path, "r", encoding="utf-8-sig") as f:
    style_min_content = f.read()

# Make sure old imports are not present in style_min_content
style_min_content = re.sub(r'@import url\("[^"]+"\);', '', style_min_content)
style_min_content = re.sub(r'@import"[^"]+";', '', style_min_content)
style_min_content = style_min_content.replace('\ufeff', '')

# Prepend the inlined font styles to style.min.css
new_style_min_content = inlined_css + style_min_content

with open(style_min_path, "w", encoding="utf-8") as f:
    f.write(new_style_min_content)

print("SUCCESS: Inlined all font and icon styles into style.min.css cleanly (BOM removed!)")
print(f"Original inlined length: {len(inlined_css)} chars")
