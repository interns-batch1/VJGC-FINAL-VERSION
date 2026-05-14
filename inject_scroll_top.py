import os
import re

templates_dir = r"c:\Users\Admin\vjgc-final\vjs-website\templates"

css_block = """
	<style>
		/* ===== SCROLL TO TOP BUTTON ===== */
		.vjs-scroll-top-btn {
			position: fixed;
			bottom: 30px;
			right: 30px;
			width: 60px;
			height: 60px;
			background: linear-gradient(135deg, #A2D732 0%, #1A4137 100%);
			border: none;
			border-radius: 50%;
			color: white;
			font-size: 24px;
			display: flex;
			align-items: center;
			justify-content: center;
			cursor: pointer;
			z-index: 9999;
			opacity: 0;
			visibility: hidden;
			transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
			box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
			transform: translateY(20px);
		}

		.vjs-scroll-top-btn.visible {
			opacity: 1;
			visibility: visible;
			transform: translateY(0);
		}

		.vjs-scroll-top-btn:hover {
			transform: translateY(-5px) scale(1.05);
			box-shadow: 0 15px 40px rgba(162, 215, 50, 0.4);
			color: #fff;
		}

		.vjs-scroll-top-btn i {
			line-height: 1;
		}

		@media (max-width: 768px) {
			.vjs-scroll-top-btn {
				width: 50px;
				height: 50px;
				bottom: 20px;
				right: 20px;
				font-size: 20px;
			}
		}
	</style>
"""

html_js_block = """
	<button id="vjs-scroll-top" class="vjs-scroll-top-btn" aria-label="Scroll to top">
		<i class="bi bi-chevron-double-up"></i>
	</button>

	<script>
		document.addEventListener('DOMContentLoaded', function () {
			const scrollTopBtn = document.getElementById('vjs-scroll-top');
			if (!scrollTopBtn) return;

			window.addEventListener('scroll', function () {
				if (window.pageYOffset > 400) {
					scrollTopBtn.classList.add('visible');
				} else {
					scrollTopBtn.classList.remove('visible');
				}
			});

			scrollTopBtn.addEventListener('click', function () {
				window.scrollTo({
					top: 0,
					behavior: 'smooth'
				});
			});
		});
	</script>
"""

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "vjs-scroll-top" in content:
        print(f"Skipping {os.path.basename(file_path)} - already has scroll-top")
        return

    # Insert CSS before </head>
    if "</head>" in content:
        content = content.replace("</head>", f"{css_block}</head>")
    
    # Insert HTML/JS before </body> or end of file
    if "</body>" in content:
        content = content.replace("</body>", f"{html_js_block}</body>")
    elif "</div> <!-- /.main-page-wrapper -->" in content:
        content = content.replace("</div> <!-- /.main-page-wrapper -->", f"{html_js_block}</div> <!-- /.main-page-wrapper -->")
    else:
        content += html_js_block

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {os.path.basename(file_path)}")

for filename in os.listdir(templates_dir):
    if filename.endswith(".html") and not filename.endswith(".bak"):
        process_file(os.path.join(templates_dir, filename))
