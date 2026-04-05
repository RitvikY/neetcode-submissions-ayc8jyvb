class LRUCache:

    def __init__(self, capacity: int):

        self.lru = {'cap': capacity}
        self.order = []

    def get(self, key: int) -> int:
        if key in self.lru:        # Check if updating
            self.order.remove(key) # Remove old reference
            self.order.append(key)     # Add to the fresh end
        return self.lru.get(key, -1)
        

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            self.order.remove(key)
            self.order.append(key)
            self.lru[key] = value
            return
            
        capacity = self.lru.get('cap') -1

        if len(self.lru) > capacity + 1:
            removed = self.order.pop(0)
            self.lru.pop(removed)
        self.lru[key] = value
        self.order.append(key)     # Add to the fresh end


        return None
        
