class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1

        while left <= right:
            print(left, right)
            nLeft = numbers[left]
            nRight = numbers[right]

            if nLeft + nRight == target:
                return [left + 1, right + 1]
            elif nLeft + nRight < target:
                left += 1
            else:
                right -=1
            
        return []