import urllib.request

try:
    url = "http://127.0.0.1:5006/"
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')
    print("Page fetched successfully!")
    
    # Check if the new mission statement is in the HTML
    new_text = "To deliver innovative and reliable solutions through technology, expertise, and customer-focused services, empowering business to achieve sustainable growth"
    if new_text in html:
        print("Success! The new mission text is on the home page.")
    else:
        print("Failure! The new mission text was NOT found on the home page.")
        
    # Check if the old mission statement is in the HTML
    old_text = "To deliver innovative and reliable solutions across diverse industries"
    if old_text in html:
        print("Warning: The old mission text is still on the home page.")
    else:
        print("Good: The old mission text is gone.")
        
except Exception as e:
    print(f"Error fetching page: {e}")
