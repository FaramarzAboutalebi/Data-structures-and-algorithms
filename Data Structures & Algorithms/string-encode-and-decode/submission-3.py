from typing import List

class Solution:
    def encode(self, strs: List[str])->str:
        # time complexity: O(L)
        # space complexity: O(L)
        res = []
        
        for w in strs:
            res.append(str(len(w)))
            res.append('#')   
            res.append(w)
        
        return "".join(res)
        
    def decode(self, s: str)->List[str]:
        # time complexity: O(L)
        # space complexity: O(L)
        i = 0 
        res = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
                
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            
            i = j+1+length
        return res
strs = ["neet","code","love","you"]     
res = Solution().encode(strs)
print(res) 
res = Solution().decode(res)
print(res)