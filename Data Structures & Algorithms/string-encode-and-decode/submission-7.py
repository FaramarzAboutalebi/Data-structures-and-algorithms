class Solution:

    def encode(self, strs: List[str]) -> str:

        # time complexity: O(n * m)
        # space complexity: O(n * m)

        res = []

        for s in strs:
            res.append(str(len(s)) + "#" + s)
        return "".join(res)



    def decode(self, s: str) -> List[str]:

        # time complexity: O(n * m)
        # space complexity: O(n * m)


        i = 0
        res = []
        while i < len(s):

            j = i + 1
            while j < len(s) and s[j] != "#":
                j += 1
            
            length = int(s[i:j])

            res.append(s[j+1:j+1+length])

            i = j+1+length

        return res










