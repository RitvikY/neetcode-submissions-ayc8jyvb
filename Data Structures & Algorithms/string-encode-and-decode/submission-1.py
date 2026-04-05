class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # Structure: Length + Delimiter + Word
            # Example: "Code" -> "4#Code"
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            # 1. Find the delimiter '#'
            j = i
            while s[j] != '#':
                j += 1
            
            # 2. Parse the length (everything from start up to #)
            # The number is between index 'i' and 'j'
            length = int(s[i:j])
            
            # 3. Extract the word
            # Start: j + 1 (character after #)
            # End: j + 1 + length
            word = s[j + 1 : j + 1 + length]
            res.append(word)
            
            # 4. Move pointer to the start of the NEXT segment
            i = j + 1 + length
            
        return res