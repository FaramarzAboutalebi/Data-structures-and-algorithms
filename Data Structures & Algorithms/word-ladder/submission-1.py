from collections import defaultdict,deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        wordSet = set(wordList) # T: O(N) # S: O(N * L)

        if endWord not in wordSet:
            return 0
        
        q = deque([(beginWord,1)])

        while q: # T: O(N)

            word,step = q.popleft()

            if word == endWord:
                return step
            
            for i in range(len(word)): # O(L)
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + ch + word[i+1:] # O(L)

                    if newWord in wordSet:
                        wordSet.remove(newWord)
                        q.append((newWord, step+1))
        return 0


# time complexity: O(N * L^2)
# space complexity: O(N * L)