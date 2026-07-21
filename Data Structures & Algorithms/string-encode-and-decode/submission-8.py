class Solution:

    def encode(self, strs: List[str]) -> str:

        # time complexity: O(T)
        # space complexity: O(T)
        res = []
        for s in strs:
            res.append(str(len(s))+"#"+s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        # time complexity: O(T)
        # space complexity: O(T)
        r = 0
        l = 0
        res = []

        while r < len(s):
            
            while s[r] != "#":
                r += 1
         
            length = int(s[l:r])
            res.append(s[r+1 : r+1+length])
            r, l = r+1+length,r+1+length
    
        return res

