

class Solution:
    def minWindow(self, s: str, t: str)->str:
        
        if len(s) == 0 or len(t) == 0:
            return ""
            
        window, count_t = {}, {}
        
        for c in t:
            count_t[c] = count_t.get(c,0) + 1
        
        have,need = 0, len(count_t)
        resLen = float("inf")
        res = [-1,-1]
        l = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r],0) + 1
            
            if window[s[r]] == count_t.get(s[r],0):
                have += 1   
                
            while have == need:
                if (r-l+1) < resLen:
                    resLen = r-l+1
                    res = [l,r]
                window[s[l]] -= 1
                if window[s[l]] < count_t.get(s[l],0):
                    have -= 1
                l += 1
        l,r = res[0],res[1]
        return s[l:r+1] if resLen != float("inf") else ""
# time complexity: O(n+m)
# space complexity: O(n+m)
s = "OUZODYXAZV"
t = "XYZ"       
print(Solution().minWindow(s,t))
s = "xyz"
t = "xyz"
print(Solution().minWindow(s,t))
s = "x"
t = "xy"
print(Solution().minWindow(s,t))
