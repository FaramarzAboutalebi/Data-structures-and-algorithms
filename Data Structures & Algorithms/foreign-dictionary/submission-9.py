from collections import defaultdict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
# time complexity: O(T + E + V)
# space complexity: O(T + E)
        adj = {c: set() for word in words for c in word}

        for i in range(1,len(words)):
            word2 = words[i] 
            word1 = words[i-1]

            minLen = min(len(word1),len(word2))

            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""

            for j in range(minLen):
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    break

        res = []
        visit = {}

        def dfs(char):
            if char in visit:
                return visit[char]
            
            visit[char] = True

            for nieChar in adj[char]:
                if dfs(nieChar):
                    return True

            visit[char] = False
            res.append(char)


        for char in adj:
            if dfs(char):
                return ""
        res.reverse()
        return "".join(res)
