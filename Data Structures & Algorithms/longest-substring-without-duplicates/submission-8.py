class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # intilaalize a set
        # as you go through, add until you reach a duplicate
        # record len of set until you get to the end


        stack = set()

        left, right = 0, 0

        res = 0
        curr = 0
        while right < len(s):
            if s[right] in stack:
                stack.remove(s[left])
                left += 1

            else:
                stack.add(s[right])

                right += 1
                curr = len(stack)

            res = max(res, curr)

        
        return res




        