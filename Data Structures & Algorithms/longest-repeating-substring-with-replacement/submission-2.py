class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # store in hashmap

        count = {}
        l = 0
        res = 0
        for r in range (len(s)):

            count[s[r]] = 1 + count.get(s[r], 0)
            windowLen = (r-l) + 1

            print(count)
            print(windowLen)
            print((windowLen - max(count.values())))

            while (windowLen - max(count.values())) > k:
                count[s[l]] -= 1
                l += 1
                windowLen -=1

            res = max(res, windowLen )

        return res

