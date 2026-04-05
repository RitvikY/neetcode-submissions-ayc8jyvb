class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        '''
        we need to find k

        if a pile is less then k you can finish it

        how does this relate to binary search??        

        '''
        left, right = 1,  max(piles)
        currK = 0
        while left <= right:
            k = (right + left) // 2
            time = 0
            for i in range(len(piles)):
                time += math.ceil(piles[i] / k )
            if time <= h:
                currK = k
                right = k-1
            else:
                left = k +1
        return currK
               
                



        