from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagramsDict = defaultdict(list)

        for s in strs:
            counter = [0] * 26

            for ch in s:
                idx = ord(ch) - ord('a')
                counter[idx] += 1
            
            anagramsDict[tuple(counter)].append(s)
        
        return list(anagramsDict.values())
        
# time complexity: O(n * L)
# space complexity: O(n * L)