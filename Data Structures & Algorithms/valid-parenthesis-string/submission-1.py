class Solution:
    def checkValidString(self, s: str) -> bool:

        rightMax = 0 # max possible number of unmatched
        leftMax = 0 # min possible number of unmatched

        for c in s:
            if c == '(':
                rightMax,leftMax = rightMax+1, leftMax+1
            elif c == ")":
                rightMax,leftMax = rightMax-1, leftMax-1
            else: # *
                rightMax,leftMax = rightMax+1, leftMax-1
            if leftMax < 0:
                leftMax = 0
            if rightMax < 0:
                return False
        return leftMax == 0