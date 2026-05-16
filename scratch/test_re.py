import re
text = "abc"
# group 1 = a
result = re.sub(r'(a)bc', r'\112', text)
print(f"Result: {result}")
