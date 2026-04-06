class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = []

        for s in strs:
            sorted_strs.append("".join(sorted(s)))

        res = defaultdict(list)

        for i, s in enumerate(sorted_strs):
            res[s].append(strs[i])
        
        return list(res.values())
