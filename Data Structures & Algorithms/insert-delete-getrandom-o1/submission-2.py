class RandomizedSet:

    def __init__(self):
        self.rset = set()

    def insert(self, val: int) -> bool:
        if val in self.rset:
            return False

        self.rset.add(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.rset:
            return False

        self.rset.discard(val)

        return True
        

    def getRandom(self) -> int:
        immutable_sequence = tuple(self.rset)
        return random.choice(immutable_sequence)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()