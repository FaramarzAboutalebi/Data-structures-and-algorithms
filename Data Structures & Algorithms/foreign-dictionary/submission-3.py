from typing import List

class Solution:
    def foreignDictionary(self, words: List[str])->str:
        
        adj = {c: set() for w in words for c in w}
        
        for i in range(1,len(words)):
            w1,w2 = words[i-1],words[i]
            minVal = min(len(w1),len(w2))
            
            if len(w1) > len(w2) and w1[:minVal] == w2[:minVal]: 
                return ""
            for j in range(minVal):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        visit = {}
        res = []
        def dfs(char):
            if char in visit:
                return visit[char]
            visit[char] = True    
            for neiChar in adj[char]:
                if dfs(neiChar):
                    return True
                
            res.append(char)
            visit[char] = False
            return visit[char]
        for char in adj:
            if dfs(char):
                return ""
        res = res[::-1]
        return "".join(res)

# time complexity: O(N+V+E)
# space complexity: O(V + E) 
        
                    