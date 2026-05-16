import os

def fix_corruption():
    target_dirs = [
        'c:/Users/Admin/vjgc-final/vjs-website',
        'c:/Users/Admin/vjgc-final/vjs-website/templates'
    ]

    # The corrupted string
    corrupted = "J0pxŠ0pxÌpx;"
    
    # The correct replacement
    correct = """.logo-circle {
			width: 120px;
			height: 120px;
			border: 1px solid rgba(220, 38, 38, 0.2);
			border-radius: 50%;
			padding: 14px;"""

    for directory in target_dirs:
        if not os.path.exists(directory):
            continue
            
        for filename in os.listdir(directory):
            if filename.endswith('.html'):
                filepath = os.path.join(directory, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()

                    if corrupted in content:
                        new_content = content.replace(corrupted, correct)
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Fixed: {filename}")
                except Exception as e:
                    print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    fix_corruption()
