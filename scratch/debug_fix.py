import os
import re

def debug_find():
    filepath = 'c:/Users/Admin/vjgc-final/vjs-website/templates/index-2.html'
    with open(filepath, 'rb') as f:
        data = f.read()
    
    # Try to find J0px
    index = data.find(b'J0px')
    if index != -1:
        print(f"Found J0px at {index}")
        print(f"Context: {data[index:index+20]}")
    else:
        print("Not found J0px")

if __name__ == "__main__":
    debug_find()
