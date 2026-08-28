class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1



        while l <= r:

            while l <= r and not self.isAlphaNumeric(s[l]):
                l += 1
            while l <= r and not self.isAlphaNumeric(s[r]):
                r -= 1
            
            if l <= r and s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


    def isAlphaNumeric(self, char: str)->bool:
        return ('a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9')


# time complexity: O(n)
# space complexity: O(1)