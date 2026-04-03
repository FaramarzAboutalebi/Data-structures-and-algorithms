
class Solution:
    def isValid(self, s: str)->bool:
        
        openToClose = {'(':')','[':']','{':'}'}
        stack = []
        
        for c in s:
            if c in openToClose:# open
                stack.append(c) #O(1)
            elif c in openToClose.values():
                if stack and openToClose[stack[-1]] == c:
                    stack.pop() #O(1)
                else:
                    return False
            else:
                return False
        return len(stack) == 0
        
# time complexity: O(n)
# space complexity: O(n) for stack
s = "([{}])"        
print(Solution().isValid(s))
s = "[(])"
print(Solution().isValid(s))

            