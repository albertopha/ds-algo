class Node:
    
    def __init__(self, val):
        self.val = val
        self.is_word = False
        self.next = dict()

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s or not wordDict:
            return False
        
        memo = [None for _ in range(len(s))]
        trie = self.buildTrie(wordDict)
        return self.dfs(s, 0, trie, memo)
    
    def dfs(self, s: str, start: int, trie: dict, memo: List[bool]) -> bool:
        if start >= len(s):
            return True
        
        if memo[start] is not None:
            return memo[start]
        
        for end in range(start+1, len(s)+1):
            memo[start] = self.isValid(s, start, end, trie) and\
                self.dfs(s, end, trie, memo)
            
            if memo[start]:
                return True
        memo[start] = False
        return False
            
    
    def isValid(self, s: str, start: int, end: int, trie: dict) -> bool:
        tmp = trie
        for i in range(start, end):
            if s[i] not in tmp.next:
                return False
            tmp = tmp.next[s[i]]
        return tmp.is_word
    
    def buildTrie(self, wordDict: List[str]) -> dict:
        trie = Node("")
        
        for word in wordDict:
            tmp = trie
            for char in word:
                if char not in tmp.next:
                    tmp.next[char] = Node(char)
                tmp = tmp.next[char]
            tmp.is_word = True
        return trie
