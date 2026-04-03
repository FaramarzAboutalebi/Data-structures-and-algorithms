from typing import List



class Solution:
    def encode(self, strs: List[str])->str:
        # time complexity: O(n*L)
        # space complexity: O(n*L)
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)
        
    def decode(self, s: str)->List[str]:
        # time complexity: O(n*L)
        # space cpmplexity: O(n*L)
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            j += 1
            
            res.append(s[j: j+length])
            i = j+length
        return res
  
strs = ["neet","code","love","you"]
print(Solution().encode(strs))
print(Solution().decode("4#neet4#code4#love3#you"))
          