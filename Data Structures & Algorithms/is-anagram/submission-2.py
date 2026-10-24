class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        counterS = {}
        counterT = {}
        
        for i in range(len(s)):
            
            counterS[s[i]] = counterS.get(s[i],0)+ 1
            counterT[t[i]] = counterT.get(t[i],0)+ 1
        
        for key,val in counterS.items():
            if val != counterT.get(key,0):
                return False
        return True