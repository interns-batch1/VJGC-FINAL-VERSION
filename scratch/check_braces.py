
content = open(r'c:\Users\Admin\vjgc-final\vjs-website\static\css\custom.css', 'r', encoding='utf-8').read()
stack = []
for i, char in enumerate(content):
    if char == '{':
        stack.append(i)
    elif char == '}':
        if not stack:
            print(f"Extra closing brace at position {i}")
        else:
            stack.pop()

if stack:
    for pos in stack:
        print(f"Unclosed opening brace starting at position {pos}")
        # Print some context
        start = max(0, pos - 50)
        end = min(len(content), pos + 100)
        print(f"Context: {content[start:end]}")
else:
    print("Braces are balanced")
