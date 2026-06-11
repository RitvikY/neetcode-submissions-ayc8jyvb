class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
         # we will first sort by number 1 in each of the lists, then go thru and merge anny combining ones
        
        if intervals is None:
            return []
        elif len(intervals) == 1:
            return intervals

        new_list = sorted(intervals, key=lambda interval: interval[0])
        res = [new_list[0]]
        

        for i in range (1, len(new_list)):
            #check for overlap
            if new_list[i][0] <= res[-1][1]:
                #[1, 4][2,3]
                res[-1][1] = max(res[-1][1], new_list[i][1])      
            else:
                res.append(new_list[i])
               
        return res      

        
        