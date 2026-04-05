class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = dict(Counter(nums))
        print(count)
        freq = [[] for i in range(len(nums)+1)]


        for key, v in count.items():
            freq[v].append(key)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for j in range(len(freq[i])):
                res.append(freq[i][j])
                if len(res) == k:
                    return res
        return []





        