import glob
import re

for filepath in glob.glob('templates/**/*.html', recursive=True):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the Bootstrap icon with the actual image logo they used
    new_logo = '''<div class="logo-icon-circle" style="border:none; background:transparent;">
                                    <img src="{{ url_for('static', filename='images/logo/vijayalakshmi-mark.png') }}?v=1.0" alt="VJS Logo" style="width:100%; height:100%; object-fit:contain;">
                                </div>'''
                                
    new_content = re.sub(r'<div class="logo-icon-circle">\s*<i class="bi bi-crown-fill"></i>\s*</div>', new_logo, content)
    
    # Also fix the bottom bar crown icon to be the actual logo mark
    new_bottom_logo = '''<img src="{{ url_for('static', filename='images/logo/vijayalakshmi-mark.png') }}?v=1.0" alt="" style="width:20px; height:20px; filter: brightness(0) saturate(100%) invert(84%) sepia(35%) saturate(760%) hue-rotate(352deg) brightness(91%) contrast(93%);">'''
    new_content = re.sub(r'<i class="bi bi-crown-fill gold-icon"></i>', new_bottom_logo, new_content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated logo in {filepath}")
