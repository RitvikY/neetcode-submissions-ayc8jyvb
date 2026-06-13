class TimeMap:

    def __init__(self):

        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        
        self.timemap[key].append((timestamp, value))



    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        

        curr = self.timemap[key]


        for i in range(len(curr)-1, -1, -1):
            if curr[i][0] <= timestamp:
                return curr[i][1]
        return ""
        
