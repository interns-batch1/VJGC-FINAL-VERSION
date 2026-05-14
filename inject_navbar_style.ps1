
# The exact navbar CSS from index-2.html (lines 34-432)
$navbarStyle = @'
	<style>
		@media (min-width: 992px) {

			.adani-nav-fx {
				padding: 0;
				align-self: top;
				margin: 0;
				background: #08201b;
				border: none !important;
				box-shadow: none !important;
				width: 100%;

				/* FIX: lock to top */
				position: fixed;
				top: 0;
				left: 0;
				z-index: 9999;
			}

			.adani-nav-fx .inner-content {
				padding: 0;
				margin: 0;
				animation: adaniNavReveal 0.75s cubic-bezier(0.22, 1, 0.36, 1);
			}

			.adani-nav-fx .top-header {
				position: relative;
				padding: 18px 20px;
				margin: 0;
				width: 100%;
				border-radius: 0;
				transition: padding 0.45s cubic-bezier(0.22, 1, 0.36, 1);
				transform: translateZ(0);
				backface-visibility: hidden;
				isolation: isolate;
			}
		}

		/* GLASS EFFECT */
		.adani-nav-fx .top-header::before {
			content: "";
			position: absolute;
			top: -4px;
			bottom: -3px;
			left: 0;
			right: 0;
			border-radius: inherit;
			background: linear-gradient(135deg,
					rgba(8, 32, 27, 0.88) 0%,
					rgba(8, 32, 27, 0.82) 50%,
					rgba(8, 32, 27, 0.88) 100%);
			backdrop-filter: blur(10px);
			-webkit-backdrop-filter: blur(10px);
			transform: translateZ(0);
			will-change: transform;
			z-index: 0;
		}

		/* HARD TOP COVER */
		.adani-nav-fx::before {
			content: "";
			position: absolute;
			top: 0;
			left: 0;
			width: 100%;
			height: 3px;
			background: #08201b;
			z-index: 10000;
			padding-top: 0%;
		}

		/* keep content above */
		.adani-nav-fx .top-header>.d-flex {
			position: relative;
			z-index: 2;
		}

		/* LOGO */
		.adani-nav-fx .logo img {
			transition: transform 0.45s ease;
			background-color: #9ec008;
			border-radius: 50%;
		}

		/* NAVBAR */
		.adani-nav-fx .navbar-nav {
			gap: 20px;
		}

		.adani-nav-fx .nav-item .nav-link {
			padding: 6px 16px;
			border-radius: 999px;
			font-size: 14px;
			color: rgba(255, 255, 255, 0.85);
			transition: all 0.35s ease;
		}

		/* HOVER */
		.adani-nav-fx .nav-item:hover>.nav-link,
		.adani-nav-fx .nav-item.nav-current>.nav-link {
			color: #dfff7c;
			transform: translateY(-0.5px);
		}

		/* HOVER INDICATOR */
		.adani-nav-fx .nav-hover-indicator {
			position: absolute;
			top: 0;
			left: 0;
			height: 100%;
			width: 0;
			border-radius: 999px;
			pointer-events: none;
			opacity: 0;
			transform: scale(0.92);
			background: linear-gradient(135deg,
					rgba(255, 255, 255, 0.18),
					rgba(255, 255, 255, 0.05));
			transition: all 0.45s cubic-bezier(0.22, 1, 0.36, 1);
		}

		/* DROPDOWN */
		.adani-nav-fx .navbar .dropdown-menu {
			margin-top: 14px;
			padding: 14px 8px;
			border-radius: 24px;
			border: 1px solid rgba(255, 255, 255, 0.05);
			background: rgba(253, 253, 253, 0.719);
			transform: translateY(18px) scale(0.96);
			clip-path: inset(0 0 100% 0 round 24px);
			transition: transform 0.45s cubic-bezier(0.22, 1, 0.36, 1),
				opacity 0.3s ease,
				visibility 0.3s ease,
				clip-path 0.45s cubic-bezier(0.22, 1, 0.36, 1);
		}

		.adani-nav-fx .navbar .dropdown:hover>.dropdown-menu {
			transform: translateY(0) scale(1);
			clip-path: inset(0 0 0 0 round 24px);
		}

		/* STICKY STATE */
		.adani-nav-fx.fixed {
			padding-top: 12px;
			background: #08201b;
		}

		.adani-nav-fx.fixed .top-header {
			padding: 12px 0;
		}

		.adani-nav-fx.fixed .top-header::before {
			top: -4px;
			bottom: -3px;
			background: linear-gradient(135deg,
					rgba(8, 32, 27, 0.96) 0%,
					rgba(8, 32, 27, 0.92) 50%,
					rgba(8, 32, 27, 0.96) 100%);
			backdrop-filter: blur(12px);
			-webkit-backdrop-filter: blur(12px);
		}

		/* LOGO SCALE */
		.adani-nav-fx.fixed .logo img {
			transform: scale(0.94);
		}

		/* MOBILE */
		@media (max-width: 991px) {
			.adani-nav-fx .top-header {
				position: relative;
				z-index: 5;
				margin: 0;
				background: #08201b;
			}
		}

		/* BODY FIX */
		html,
		body {
			margin: 0;
			padding: 0;
			background: #08201b;
		}

		/* ANIMATION */
		@keyframes adaniNavReveal {
			from {
				opacity: 0;
				transform: translateY(-18px);
			}

			to {
				opacity: 1;
				transform: translateY(0);
			}
		}
	</style>
'@

# Pattern: find </head> and inject before it
# But first remove any existing <style>...</style> block if it exists
$publicPath = 'C:\Users\ELCOT\vjs-website-\public'
$files = Get-ChildItem -Path "$publicPath\*.html" | Where-Object { $_.Name -ne 'index-2.html' }

$styleRemovePattern = '(?s)\s*<style>.*?</style>'
$headCloseTag = '</head>'

$count = 0
foreach ($file in $files) {
    $content = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)
    
    # Remove any existing <style> block first
    $content = [regex]::Replace($content, $styleRemovePattern, '', [System.Text.RegularExpressions.RegexOptions]::Singleline)
    
    # Inject navbar style just before </head>
    if ($content -match [regex]::Escape($headCloseTag)) {
        $content = $content.Replace($headCloseTag, $navbarStyle.TrimStart() + "`n" + $headCloseTag)
        [System.IO.File]::WriteAllText($file.FullName, $content, [System.Text.Encoding]::UTF8)
        Write-Host "Done: $($file.Name)"
        $count++
    } else {
        Write-Host "SKIPPED (no </head>): $($file.Name)"
    }
}

Write-Host ""
Write-Host "==================================="
Write-Host "Total pages updated: $count"
Write-Host "==================================="
