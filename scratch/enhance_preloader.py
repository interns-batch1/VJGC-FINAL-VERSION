import os
import re

def enhance_preloader_experience():
    # Define the ENHANCED JS with a minimum display time
    # This ensures the user sees the branding and gives assets more time to settle
    enhanced_js = """
		<script id="vjs-preloader-script">
			(function() {
				const startTime = Date.now();
				window.addEventListener('load', function() {
					const minDisplayTime = 2500; // Minimum time in ms to show the branded preloader
					const elapsed = Date.now() - startTime;
					const delay = Math.max(0, minDisplayTime - elapsed);

					setTimeout(() => {
						const preloader = document.getElementById('preloader');
						if (preloader) {
							preloader.style.opacity = '0';
							preloader.style.visibility = 'hidden';
							setTimeout(() => {
								preloader.style.display = 'none';
							}, 1000);
						}
						document.body.style.overflow = 'visible';
					}, delay);
				});
			})();
		</script>"""

    # We also want to ensure the loading bar fill animation is snappy but feels like it's "doing work"
    # I'll update the CSS in the head to make the fillBar animation more dynamic.
    
    target_dirs = [
        'c:/Users/Admin/vjgc-final/vjs-website/templates'
    ]

    for directory in target_dirs:
        for filename in os.listdir(directory):
            if filename.endswith('.html'):
                filepath = os.path.join(directory, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 1. Update the JS script
                if '<script id="vjs-preloader-script">' in content:
                    content = re.sub(r'<script id="vjs-preloader-script">.*?</script>', enhanced_js, content, flags=re.DOTALL)
                else:
                    content = content.replace('</body>', enhanced_js + '\n</body>')

                # 2. Update the CSS for a smoother experience
                # Specifically making the fillBar animation duration match the minDisplayTime roughly
                if '/* ===== PREMIUM BRANDED PRELOADER ===== */' in content:
                    # Update the fillBar animation duration to 2.5s to match JS delay
                    content = content.replace('animation: fillBar 4s cubic-bezier(0.65, 0, 0.35, 1) forwards;', 
                                            'animation: fillBar 2.5s cubic-bezier(0.65, 0, 0.35, 1) forwards;')

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Enhanced {filename}")

if __name__ == "__main__":
    enhance_preloader_experience()
