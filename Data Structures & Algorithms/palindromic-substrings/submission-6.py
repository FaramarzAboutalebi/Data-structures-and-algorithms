class Solution:
    def countSubstrings(self, s: str) -> int:

        counter = 0

        for i in range(len(s)):

            # odd
            l,r = i,i
            while l >=0 and r < len(s) and s[l] == s[r]:
                counter += 1
                l -= 1
                r += 1

            #even
            l,r = i, i+1
            while l >=0 and r < len(s) and s[l] == s[r]:
                counter += 1
                l -= 1
                r += 1
        return counter
        
# time complexity: O(n ^ 2)
# space complexity: O(1)