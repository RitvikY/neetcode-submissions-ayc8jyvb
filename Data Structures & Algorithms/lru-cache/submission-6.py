class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.time = 0
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.time += 1

        self.cache[key] = (self.cache[key][0], self.time)

        return self.cache[key][0]
        

    def put(self, key: int, value: int) -> None:
        self.time += 1

        if key in self.cache:
            self.cache[key] =  (value, self.time)
        else:
            if len(self.cache) >= self.capacity:

                oldest_key = None
                smallest_time = float('inf') 
                # find lowest itme stmap
                for k, (val, ts) in self.cache.items():
                    if ts < smallest_time:
                        smallest_time = ts
                        oldest_key = k
                del self.cache[oldest_key]
                

            self.cache[key] =  (value, self.time)
        
        
