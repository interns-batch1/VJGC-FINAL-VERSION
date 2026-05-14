import os

templates_dir = r"c:\Users\Admin\vjgc-final\vjs-website\templates"

def remove_scroll_top(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove CSS block
    content = content.replace('\n\t<style>\n\t\t/* ===== SCROLL TO TOP BUTTON ===== */', '/*REMOVED*/')
    # Use regex to find the end of the style block I added
    import re
    content = re.sub(r'/\* ===== SCROLL TO TOP BUTTON ===== \*/.*?</style>', '', content, flags=re.DOTALL)
    
    # Remove HTML/JS block
    content = re.sub(r'<button id="vjs-scroll-top".*?</script>', '', content, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Cleaned {os.path.basename(file_path)}")

for filename in os.listdir(templates_dir):
    if filename.endswith(".html") and not filename.endswith(".bak"):
        remove_scroll_top(os.path.join(templates_dir, filename))
