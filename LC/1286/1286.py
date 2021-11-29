"""
abcdefg
^
  ^
abd|efg
abe|fg
abf|g
abg|

acd|efg


[a,b,c,d,e,f,g]
       ^
[a,b,c]
"""
class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.index = 0
        self.combinations = []
        self.generateCombinations(characters, combinationLength, "", 0, self.combinations)

    def next(self):
        """
        :rtype: str
        """
        n = self.combinations[self.index]
        self.index += 1
        return n

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index < len(self.combinations)
    
    def generateCombinations(self, chars, combinationLen, current, index, combinations):
        if len(current) == combinationLen:
            combinations.append(current)
            return
        
        for i in range(index, len(chars)):
            self.generateCombinations(chars, combinationLen, current + chars[i], i+1, combinations)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
