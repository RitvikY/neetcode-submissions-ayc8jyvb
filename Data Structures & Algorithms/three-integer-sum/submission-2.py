class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        '''

        sort , 
        fix 1 number
        move left or right based on comparison  
        '''

        sortedNum = sorted(nums)
        res = []

         #iterate through each num as a fixed num
        for i in range (0, len(sortedNum)):
            if i != 0  and sortedNum[i] == sortedNum[i-1]:
                continue

            left = i + 1
            right = len(sortedNum) - 1 
            diff = -1 * sortedNum[i]
            while left < right:
                if sortedNum[left] + sortedNum[right] == diff:
                    res.append([sortedNum[left], sortedNum[right], sortedNum[i]])

                    while  left < right and sortedNum[left+1] == sortedNum[left]:
                        left += 1

                    while  left < right and sortedNum[right-1] == sortedNum[right]:
                        right -= 1

                    left +=1
                    right -=1
                    
                elif sortedNum[left] + sortedNum[right] < diff:
                    left += 1
                elif sortedNum[left] + sortedNum[right] > diff:
                    right -= 1
        
        return res 

                


