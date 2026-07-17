

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        counter_t = {}
        resLen,resRange = float("inf"),[-1,-1]

        for c in t:
           counter_t[c] =  counter_t.get(c,0) + 1

        need, have = len(counter_t),0
        l = 0

        counter_w = {}

        for r in range(len(s)):
            counter_w[s[r]] =  counter_w.get(s[r],0) + 1

            if counter_w[s[r]] == counter_t.get(s[r],0):
                have += 1

            while need == have:
                if (r-l+1) < resLen:
                    resLen = r-l+1
                    resRange = [l,r]
                
                # shrink it
                counter_w[s[l]] -= 1
                if counter_w[s[l]] < counter_t.get(s[l],0):
                    have -= 1
                l += 1

        l,r = resRange

        return s[l:r+1] if resLen != float("inf") else ""


# time complexity: O(n + m)
# space complexity: O(n + m) for hashmaps    