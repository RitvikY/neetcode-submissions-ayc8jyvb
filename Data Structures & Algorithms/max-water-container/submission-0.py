class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left , right = 0, len(heights) -1


        res = 0
        while left < right:

            heightL = heights[left]
            heightR = heights[right]
            volume = min(heightL, heightR) * (right - left)

            if volume > res:
                res = volume
            
            if heightL < heightR:
                left += 1
            else:
                right -= 1

        return res




