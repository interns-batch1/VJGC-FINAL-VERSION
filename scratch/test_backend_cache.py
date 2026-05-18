import time
import urllib.request

def test_cache_performance():
    url = "http://127.0.0.1:5006/"
    
    print("Testing Backend Cache Performance...")
    
    # 1. Cold Cache hit (triggers MongoDB query)
    start_time = time.time()
    req1 = urllib.request.urlopen(url)
    req1.read()
    duration1 = (time.time() - start_time) * 1000
    print(f"Cold Cache Hit (First Load): {duration1:.2f} ms")
    
    # 2. Warm Cache hit (loaded instantly from memory)
    start_time = time.time()
    req2 = urllib.request.urlopen(url)
    req2.read()
    duration2 = (time.time() - start_time) * 1000
    print(f"Warm Cache Hit (Second Load): {duration2:.2f} ms")
    
    improvement = (duration1 - duration2) / duration1 * 100
    print(f"Performance Speedup: {improvement:.2f}% faster!")
    print(f"Response Time dropped by {duration1 - duration2:.2f} ms!")

if __name__ == "__main__":
    # Wait a second for FastAPI server to reload
    time.sleep(1.5)
    test_cache_performance()
