import os

def fix_bytes():
    target_dirs = [
        'c:/Users/Admin/vjgc-final/vjs-website',
        'c:/Users/Admin/vjgc-final/vjs-website/templates'
    ]

    # The corrupted byte sequence as found by debug script
    corrupted_bytes = b'J0px\xc2\x8a0px\xc3\x8cpx;'
    
    # The correct replacement
    correct_text = """.logo-circle {
			width: 120px;
			height: 120px;
			border: 1px solid rgba(197, 160, 89, 0.2);
			border-radius: 50%;
			padding: 14px;"""
    correct_bytes = correct_text.encode('utf-8')

    for directory in target_dirs:
        if not os.path.exists(directory):
            continue
            
        for filename in os.listdir(directory):
            if filename.endswith('.html'):
                filepath = os.path.join(directory, filename)
                try:
                    with open(filepath, 'rb') as f:
                        data = f.read()

                    if corrupted_bytes in data:
                        new_data = data.replace(corrupted_bytes, correct_bytes)
                        with open(filepath, 'wb') as f:
                            f.write(new_data)
                        print(f"Fixed: {filename}")
                except Exception as e:
                    print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    fix_bytes()
