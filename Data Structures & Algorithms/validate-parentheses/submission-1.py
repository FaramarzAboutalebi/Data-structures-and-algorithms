class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        closeToOpen = {")":"(", "]":"[", "}":"{",}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False

            elif c in closeToOpen.values():
                stack.append(c)
            else:
                return False

        return len(stack) == 0
        
# time complexity: O(n)
# space complexity: O(n) for stack