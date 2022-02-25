class Node:
    
    def __init__(self, char):
        self.char = char
        self.is_word = False
        self.nexts = dict() 
    
class WordDictionary:

    def __init__(self):
        self.trie = Node('')

    def addWord(self, word: str) -> None:
        node = self.trie
        for char in word:
            if char not in node.nexts:
                node.nexts[char] = Node(char)
            node = node.nexts[char]
        node.is_word = True
          
    def search(self, word: str) -> bool:
        return self.dfs(word, 0, self.trie)
    
    def dfs(self, word: str, index: int, node: 'Node') -> bool:
        if index >= len(word):
            return node.is_word 
        
        char = word[index]
        
        if char != '.':
            if char not in node.nexts:
                return False
            return self.dfs(word, index+1, node.nexts[char])
        
        for child in node.nexts.values():
            if self.dfs(word, index+1, child):
                return True
        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
