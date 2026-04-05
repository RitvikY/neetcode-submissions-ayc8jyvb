class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        nums = sorted(nums)
        res = []
        for index, num in enumerate(nums):

            if index > 0 and num == nums[index - 1]:
                continue
            l, r = index+1, len(nums)-1

            while l < r:
                if (nums[l] + nums[r] + num) == 0:
                    res.append([nums[l], nums[r], num])
                    l +=1
                    r -=1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif (nums[l] + nums[r]+ num) > 0:
                    r -= 1
                else:
                    l += 1
        

        return res




        