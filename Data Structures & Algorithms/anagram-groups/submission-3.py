from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str])->List[List[str]]:
        
        anagramsMap = defaultdict(list)
        
        for string in strs:
            counter = [0] * 26
            
            for c in string:
                idx = ord(c) - ord('a')
                counter[idx] += 1
            
            anagramsMap[tuple(counter)].append(string)
        return list(anagramsMap.values())

# time complexity: O(n * L)
# space complexity: O(n * L)

strs = ["act","pots","tops","cat","stop","hat"]
print(Solution().groupAnagrams(strs))
