import urllib.request
import urllib.error

urls = [
    "http://127.0.0.1:5006/",
    "http://127.0.0.1:5006/static/css/style.min.css",
    "http://127.0.0.1:5006/static/fonts/bootstrap-icons-1.10.2/bootstrap-icons.woff2",
]

for url in urls:
    try:
        req = urllib.request.Request(url, method='HEAD')
        with urllib.request.urlopen(req) as resp:
            print(f"{url}: {resp.status}")
    except urllib.error.URLError as e:
        print(f"{url}: Failed - {e}")
