class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashMap = {
            "2": ["A","B","C"],
            "3": ["D","E","F"],
            "4": ["G","H","I"],
            "5": ["J","K","L"],
            "6": ["M","N","O"],
            "7": ["P","Q","R","S"],
            "8": ["T","U","V"],
            "9": ["W","X","Y","Z"]
        }

        curStr = []
        res = []

        def dfs(i):
            if i == len(digits):
                res.append("".join(curStr))
                return 
            for c in hashMap[digits[i]]:
                curStr.append(c.lower())
                dfs(i+1)
                curStr.pop()
        if digits:
            dfs(0)
        return res