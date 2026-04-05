class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        count = {}

        for s in s1:
            print(s)
            count[s] = 1 + count.get(s, 0)

        l =  0
        window_count = {}
        for r in range (len (s2)) :
            
            ## 3xpand windo
            window_count[s2[r]] = 1 + window_count.get(s2[r], 0)

            if (r-l +1) > len(s1):
                window_count[s2[l]] -= 1
                if window_count[s2[l]]  <= 0:
                    window_count.pop(s2[l], None)
                l += 1
            
            if window_count == count:
                return True
        return False






            

                
                



        
        return False
            
                    
                
            

        