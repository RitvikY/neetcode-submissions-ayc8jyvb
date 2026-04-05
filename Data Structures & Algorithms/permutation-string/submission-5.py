class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = dict(Counter(s1))


        if len(s1) > len(s2): return False
        left = 0
        right = len(s1) - 1

        s2Count = (defaultdict(int))

        for i in range (len(s1)):
            s2Count[s2[i]] += 1

        while right < len(s2):
            if s1Count == s2Count:
                return True


            right += 1

            if right < len(s2):
                s2Count[s2[right]] += 1

                # 3. NOW remove the old left element
                s2Count[s2[left]] -= 1
                if s2Count[s2[left]] == 0:
                    del s2Count[s2[left]]
                
                # 4. Move left forward to keep the window size constant
                left += 1
            

        return False


        
        
        