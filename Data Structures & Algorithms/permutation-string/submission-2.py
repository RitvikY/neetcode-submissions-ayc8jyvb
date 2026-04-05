class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1count = dict(Counter(s1))

        left, right = 0, 0

        s2count = {}
        while right < len(s2):
            s2count[s2[right]] = 1 + s2count.get(s2[right], 0)
            
            if right - left + 1 > len(s1):
                s2count[s2[left]] -= 1
                if s2count[s2[left]] == 0:
                    s2count.pop(s2[left])
                left += 1
            
            if s1count == s2count:
                return True
            
            right += 1
        return False