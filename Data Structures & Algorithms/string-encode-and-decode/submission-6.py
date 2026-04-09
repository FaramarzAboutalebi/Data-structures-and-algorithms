class Solution:

    def encode(self, strs: List[str]) -> str:

        # time complexity: O(T)
        # space compexity: O(T)
        res = []

        for s in strs:
            res.append(str(len(s)) + "#" + s)
 
        print("".join(res))
        return "".join(res)


    def decode(self, s: str) -> List[str]:
        # time complexity: O(T)
        # space compexity: O(T)
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            lenght = int(s[i:j])
            res.append(s[j+1:j+1+lenght])
            i = j+1+lenght
        return res

