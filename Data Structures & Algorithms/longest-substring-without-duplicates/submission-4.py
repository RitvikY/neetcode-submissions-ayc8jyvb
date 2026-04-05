class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left, right = 0, 0

        res = 0
        letters = set()
        while right < len(s):


            while s[right] in letters:
                letters.remove(s[left]) # Remove from the LEFT
                left += 1               # Move the window start
            
            letters.add(s[right])
            right += 1
            res = max(res, len(letters))

        return res



        