class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        fleet = [[0, 0] for i in range(len(position))]

        for i in range(len(position)):
            fleet[i][0] = position[i]
            fleet[i][1] = speed[i]

        fleet = sorted(fleet, reverse=True)
        

        stack = []

        for n in range (0, len(fleet)):
            time = (target - fleet[n][0])/fleet[n][1]

            if len(stack) == 0:
                stack.append(time)

            elif time > stack[-1]:
                stack.append(time)
        
        return len(stack)