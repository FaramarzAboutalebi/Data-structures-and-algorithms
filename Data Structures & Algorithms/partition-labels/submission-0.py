class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        lasIndex = {}

        for i in range(len(s)):
            lasIndex[s[i]] = i
        res = []
        size,end = 0,0

        for i in range(len(s)):
            size += 1
            end = max(end, lasIndex[s[i]])
            if i == end:
                res.append(size)
                size = 0
        return res