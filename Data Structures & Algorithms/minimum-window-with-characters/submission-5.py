class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # s = ABDCBCA -> len = n        {A:1, B: 0, D: 0, C: 1} l = 1,r=3
        # t = CBA -> len = m            {A:1, B:1, C:1}. need = 3, have = 3

        resLen, resRange = float("inf"), [-1,-1]
        counter_window, counter_t = {}, {}

        for c in t: # O(m)
            counter_t[c] = counter_t.get(c,0) + 1
        
        have,need = 0, len(counter_t)

        l = 0 

        for r in range(len(s)):

            counter_window[s[r]] = counter_window.get(s[r], 0)+ 1

            if counter_window[s[r]] == counter_t.get(s[r],0):
                have += 1
            
            while have == need:
                if (r-l+1) < resLen:
                    resLen = r-l+1
                    resRange = [l,r]
                
                counter_window[s[l]] -= 1
                if counter_window[s[l]] < counter_t.get(s[l],0):
                    have -= 1
                l += 1

        l,r = resRange[0],resRange[1]

        return s[l:r+1] if resLen != float("inf") else ""

# time complexity: O(n + m)
# space complexity: O(n + m)

        