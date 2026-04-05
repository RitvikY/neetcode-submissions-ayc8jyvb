class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        have a hashamp with characters
        find the smallest value, if its <= k, get the total vlaues
        otherwise, update the hasmap

        '''
        
        res = 0
        left = 0
        charMap = defaultdict(int)
        max_f = 0

        for right in range(len(s)):
            max_f = max(max_f, charMap[s[right]])
            charMap[s[right]] += 1            
            while (right - left )  - max_f > k:
                charMap[s[left]] -= 1
                left += 1
            

            res = max(res, sum(charMap.values()))
        
        return res 
            
