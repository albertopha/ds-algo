from collections import defaultdict

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s or not wordDict:
            return []
        
        charMap = defaultdict(list)
        for word in wordDict:
            charMap[word[0]].append(word)
        
        words = []
        self.helper(s, 0, charMap, [], words)
        return words
        
    def helper(self, s: str, i: int, charMap: dict, word: List[str], words: List[str]) -> None:
        if i >= len(s):
            words.append(" ".join(word))
            return
        
        if s[i] not in charMap:
            return
        
        for nextWord in charMap[s[i]]:
            if not s.startswith(nextWord, i):
                continue
            
            word.append(nextWord)
            self.helper(s, i+len(nextWord), charMap, word, words)
            word.pop()
                
            
