import random
    
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.index_map = dict()
        self.values = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.index_map:
            return False
        
        self.values.append(val)
        self.index_map[val] = len(self.values) - 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        ""
        if val not in self.index_map:
            return False
        
        i = self.index_map[val]
        last_elem = self.values[-1]
        self.values[-1], self.values[i] = self.values[i], self.values[-1]
        self.index_map[last_elem] = i
        self.values.pop()
        del self.index_map[val]
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        rand = random.randint(0, len(self.values)-1)
        return self.values[rand]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
