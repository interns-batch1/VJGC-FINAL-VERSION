import os
from PIL import Image
import shutil

# Paths
STATIC_DIR = r"c:\Users\Admin\vjgc-final\vjs-website-\static"
BACKUP_DIR = r"c:\Users\Admin\vjgc-final\vjs-website-\static_backup"

# Thresholds
SIZE_THRESHOLD_MB = 1.0  # Compress any image > 1MB
MAX_WIDTH = 1920         # Max width for web use
QUALITY = 80             # JPEG quality

def compress_images():
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
        print(f"Created backup directory: {BACKUP_DIR}")

    print(f"Scanning for large images in {STATIC_DIR}...")
    
    count = 0
    total_saved = 0

    for root, dirs, files in os.walk(STATIC_DIR):
        # Skip backup dir if it's inside static (though it shouldn't be here)
        if "static_backup" in root:
            continue

        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                filepath = os.path.join(root, file)
                filesize_mb = os.path.getsize(filepath) / (1024 * 1024)

                if filesize_mb > SIZE_THRESHOLD_MB:
                    print(f"\nOptimizing: {file} ({filesize_mb:.2f} MB)")
                    
                    # Create backup path
                    rel_path = os.path.relpath(root, STATIC_DIR)
                    backup_root = os.path.join(BACKUP_DIR, rel_path)
                    if not os.path.exists(backup_root):
                        os.makedirs(backup_root)
                    
                    backup_path = os.path.join(backup_root, file)
                    
                    # Backup original
                    shutil.copy2(filepath, backup_path)
                    
                    # Compress
                    try:
                        with Image.open(filepath) as img:
                            # Resize if too wide
                            if img.width > MAX_WIDTH:
                                ratio = MAX_WIDTH / float(img.width)
                                new_height = int(float(img.height) * float(ratio))
                                img = img.resize((MAX_WIDTH, new_height), Image.Resampling.LANCZOS)
                                print(f"  - Resized to {MAX_WIDTH}px wide")
                            
                            # Convert RGBA to RGB if saving as JPEG
                            if img.mode in ("RGBA", "P"):
                                img = img.convert("RGB")
                            
                            img.save(filepath, "JPEG", quality=QUALITY, optimize=True)
                        
                        new_size_mb = os.path.getsize(filepath) / (1024 * 1024)
                        saved = filesize_mb - new_size_mb
                        print(f"  - Done! New size: {new_size_mb:.2f} MB (Saved {saved:.2f} MB)")
                        
                        count += 1
                        total_saved += saved
                    except Exception as e:
                        print(f"  - Error processing {file}: {e}")

    print(f"\n--- Summary ---")
    print(f"Total images optimized: {count}")
    print(f"Total space saved: {total_saved:.2f} MB")
    print(f"Original files are backed up in: {BACKUP_DIR}")

if __name__ == "__main__":
    compress_images()
