

class Solution:
    def isPalindrome(self, s: str)->bool:
        
        l,r = 0, len(s)-1
        while l <= r:
            while l <= r and not self.alphanumeric(s[l]):
                l += 1
            while l <= r and not self.alphanumeric(s[r]):
                r -= 1
            if l <= r and s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
            
    def alphanumeric(self, char: str)->bool:
        if ('a' <= char <= 'z' or 
            'A' <= char <= 'Z' or
            '0' <= char <= '9'):
                return True
        return False
# time complexity: O(n)
# space complexity: O(1)
s = "Was it a car or a cat I saw?"        
print(Solution().isPalindrome(s))

s = "tab a cat"
print(Solution().isPalindrome(s))



