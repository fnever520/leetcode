"""
given a list of n items accessed in sequence from a system, and a cache with Least recently user (LRU) replacement policy. 
The goal is to determine the minimum cache size required to ensure at least k requests hit the cache. if it is not possible to achieve k hits, return -1.

Suppose n=1, requests = ["item1", "item1", "item3", "item1", "item3"], and k = 1

with size of cache as 1, we get 1
"""

from collections import deque  
  
def min_cache_size(n, requests, k):  
    for size in range(1, n+1):  
        cache = {}  
        queue = deque()  
        hits = 0  
          
        for item in requests:  
            if item in cache:  
                # Update the access time of the item in the cache  
                queue.remove(item)  
                queue.append(item)  
                cache[item] += 1  
                hits += 1  
            else:  
                # Add the item to the cache  
                if len(cache) == size:  
                    # Remove the least recently used item from the cache  
                    lru_item = queue.popleft()  
                    del cache[lru_item]  
                queue.append(item)  
                cache[item] = 1  
              
            if hits >= k:  
                return size  
      
    return -1  

n = 5
requests = ["item3", "item2", "item1", "item2", "item3"]  
k = 1
result = min_cache_size(n, requests, k)  
print(result)