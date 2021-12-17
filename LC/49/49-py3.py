class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        
        dictionary = dict()
        anagrams = []
        
        for word in strs:
            key = self.getKey(word)
            if key not in dictionary:
                anagrams.append([])
                dictionary[key] = len(anagrams)-1
            index = dictionary[key]
            anagrams[index].append(word)
        return anagrams
        
    def getKey(self, word: str) -> str:
        return str(sorted(list(word)))
