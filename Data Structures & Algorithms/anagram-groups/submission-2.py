from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str])->List[List[str]]:
        
        anagramDict = defaultdict(list)
        
        for w in strs:
            counter = [0] * 26
            for c in w:
                idx = ord(c)-ord('a')
                counter[idx] += 1
            
            anagramDict[tuple(counter)].append(w)  
        return list(anagramDict.values())
# time complexity: O(n*m)
#space complexity:O(n)
strs = ["act","pots","tops","cat","stop","hat"]
print(Solution().groupAnagrams(strs))




        