with open(r"c:\Users\Admin\vjgc-final\vjs-website\static\css\custom.css", "r", encoding="utf-8") as f:
    content = f.read()

open_braces = content.count("{")
close_braces = content.count("}")

print(f"Open braces: {open_braces}")
print(f"Close braces: {close_braces}")

if open_braces != close_braces:
    print("Mismatched braces detected!")
else:
    print("Braces match.")
