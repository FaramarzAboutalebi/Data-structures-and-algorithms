class Solution:
    
    def isPalindrome(self, s: str)->bool:
        
        l, r = 0, len(s) - 1
        
        while l <= r:
            while l <= r and not self.isAlphanumeric(s[l]):
                l += 1
                
            while l <= r and not self.isAlphanumeric(s[r]):
                r -= 1
                
            if l <= r and s[l].lower() != s[r].lower():
            
                return False
            l += 1
            r -= 1
        return True
        
    def isAlphanumeric(self, ch: str)->bool:
        if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z' or '0' <= ch <= '9':
            return True
        return False
# time complexity: O(L)
# space complexity: O(1)
s = "Was it a car or a cat I saw?"        
print(Solution().isPalindrome(s))
s = "tab a cat"
print(Solution().isPalindrome(s))
s="Madam, in Eden, I'm Adam"
print(Solution().isPalindrome(s))

            