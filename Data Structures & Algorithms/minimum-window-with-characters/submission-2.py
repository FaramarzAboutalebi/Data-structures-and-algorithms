class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        counter_window,counter_t = {},{}
        resLen = float("inf")
        res_range = [-1,-1]


        for c in t:
            counter_t[c] = counter_t.get(c,0) + 1

        have, need = 0, len(counter_t)

        l = 0

        for r in range(len(s)):
            counter_window[s[r]] = counter_window.get(s[r],0) + 1

            if counter_window[s[r]] == counter_t.get(s[r],0):
                have += 1
            
            while need == have:
                if (r-l+1) < resLen:
                    resLen = r-l+1
                    res_range = [l,r]

                counter_window[s[l]] = counter_window.get(s[l], 0) - 1
                

                if counter_window[s[l]] < counter_t.get(s[l],0):
                    have -= 1

                l += 1
        l,r = res_range

        return s[l:r+1] if resLen != float("inf") else ""
                



# time complexity: O(n + m)
# space complexity: O(n + m)
