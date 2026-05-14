$f = 'C:\Users\ELCOT\vjs-website-\public\about-us-v1.html'
$c = [System.IO.File]::ReadAllText($f, [System.Text.Encoding]::UTF8)

$results = @(
    "Navbar HTML (adani-nav-fx)   : " + ($c -match 'adani-nav-fx')
    "Logo lockup                  : " + ($c -match 'site-brand-lockup')
    "Get in Touch button          : " + ($c -match 'Get in Touch')
    "Flat CSS (border-radius: 0)  : " + ($c -match 'border-radius: 0')
    "Hover JS (navbar-hover.js)   : " + ($c -match 'navbar-hover\.js')
    "Dark glass background        : " + ($c -match 'rgba\(8, 32, 27, 0\.88\)')
    "Slide animation keyframe     : " + ($c -match 'adaniNavReveal')
    "Fixed position CSS           : " + ($c -match 'position: fixed')
)

Write-Host "=== about-us-v1.html Verification ===`n"
foreach ($r in $results) {
    if ($r -match 'True$') {
        Write-Host "  [PASS] $r"
    } else {
        Write-Host "  [FAIL] $r"
    }
}
