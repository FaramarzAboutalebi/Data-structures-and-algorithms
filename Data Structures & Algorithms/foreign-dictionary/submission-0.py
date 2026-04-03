from typing import List
from collections import defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]):
        if not words:
            return ""
            
        res = []
        edges = {c: set() for w in words for c in w}
        
        for i in range(1,len(words)):
            w1 = words[i-1]
            w2 = words[i]
            minLen = min(len(w1),len(w2))
            
            for j in range(minLen):
                if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                    return ""
                elif w1[j] != w2[j]:
                    edges[w1[j]].add(w2[j])
                    break
        visited = {}
        
        def dfs(char):
            if char in visited:
                return visited[char]
            visited[char] = True
            for nei in edges[char]:
                if dfs(nei):
                    return True # cycle
            visited[char] = False
            res.append(char)
            
    
        for char in edges:
            if dfs(char):
                return ""
        res = res[::-1]
        return "".join(res)
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
            
    