
from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]):
        
        anagramDic = defaultdict(list)
        
        for string in strs:
            counter = [0] * 26
            for c in string:
                idx = ord(c) - ord('a')
                counter[idx] += 1
            anagramDic[tuple(counter)].append(string)
        return list(anagramDic.values())
# n: number of words, m number of char a
# time complexity: O(n.m)
# space complexity: O(n.m)
strs = ["act","pots","tops","cat","stop","hat"]
print(Solution().groupAnagrams(strs))
                