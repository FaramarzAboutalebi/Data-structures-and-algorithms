class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) == 0 or len(t) == 0:
            return ""

        window,counter_t = {},{}

        for ch in t:
            counter_t[ch] = counter_t.get(ch,0) + 1

        have,need = 0, len(counter_t)
        l = 0

        res = float("inf")
        bound = [-1,-1]

        for r in range(len(s)):
            window[s[r]] = window.get(s[r],0) + 1

            if window[s[r]] == counter_t.get(s[r],0):
                have += 1
            
            while have == need:
                if (r-l+1) < res:
                    res = r-l+1
                    bound = [l,r]
                window[s[l]] -= 1
                if window[s[l]] < counter_t.get(s[l],0):
                    have -= 1
                l += 1
        l,r = bound[0],bound[1]

        return s[l:r+1] if res != float("inf") else ""
# time complexity: O(|s| + |t|)
# space complexity: O(k)
        

        