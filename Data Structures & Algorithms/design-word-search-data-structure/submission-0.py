class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        
class WordDictionary:
    ##
    def __init__(self):
        self.root = TrieNode()
    ##  
    def addWord(self, word: str)->None:
        # time complexity: O(L)
        # space complexity: O(L)

        cur = self.root
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True 

    ##
    def search(self, word: str)->bool:
        # time complexity: O(L) it can become 26^L in the worst case
        # space complexity: O(L)

        def dfs(i, cur):
            if i >= len(word):
                return cur.endOfWord
            c = word[i]
            if c == '.':
                for child in cur.children.values():
                    if dfs(i+1, child):
                        return True
                return False
            else:
                if c not in cur.children:
                    return False
                return dfs(i+1,cur.children[c])
            
        return dfs(0, self.root)
trie = WordDictionary()
trie.addWord("day")
trie.addWord("bay")
trie.addWord("may")
print(trie.search("say")) # return false
print(trie.search("day")) # return true
print(trie.search(".ay")) # return true
print(trie.search("b..")) # return true