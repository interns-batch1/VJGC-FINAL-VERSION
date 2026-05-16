import os

def fix_bytes():
    target_dirs = [
        'c:/Users/Admin/vjgc-final/vjs-website',
        'c:/Users/Admin/vjgc-final/vjs-website/templates'
    ]

    # The corrupted byte sequence
    # \112 -> 0x4A (J)
    # \212 -> 0x8A
    # \314 -> 0xCC
    corrupted_bytes = b'\x4A0px\x8A0px\xCCpx;'
    
    # The correct replacement
    correct_text = """.logo-circle {
			width: 120px;
			height: 120px;
			border: 1px solid rgba(220, 38, 38, 0.2);
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
                        print(f"Fixed (bytes): {filename}")
                except Exception as e:
                    print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    fix_bytes()
