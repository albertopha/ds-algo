"""
=======================================================
Test cases:
#1
capacity = 2
put -> [2, 2], [1, 3], [1, 4]
get -> [1] returns 3
get -> [2] returns 2

=======================================================
Brute force:
1. PUT: array of tuples (key, value) -- O(1)
    a. if the len(array) > capacity,
        remove the first element. -- O(1)
2. GET:
    a. search through the array and find the key. -- O(N)
        Once found, return the value.
    b. move the pair to the end of the array. -- O(N)
    
Time: O(1) for put, O(N)
Space: O(N)
=======================================================
Optimal:
data structures to use:
- Doubly linked list for insert and remove node.
- Map (dict) for searching for the key.

1. PUT: map[key] points to te node of the linked list
    (saves the address in the memory). -- O(1)

2. GET:
    map[key] gives us the node -> move to the end list
    return the value. -- O(1)
    
Time: O(1)
Space: O(1)
=======================================================
"""

class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = Node

        
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.size = 0
        self.capacity = capacity
        self.head = Node('h', 0)
        self.tail = Node('t', 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.size == 0 or\
            key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.move_to_end(node)
        # print('=============== GET ========== ')
        # print(self.cache)
        # print(self.head.next.value)
        # print(self.tail.prev.value)
        # print('======================== ')
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            # Simply update the value
            node = self.cache[key]
            node.value = value
            self.move_to_end(node)
            return
        
        new_node = Node(key, value)
        if self.size == self.capacity:
            least_frequent_node_key = self.head.next.key
            self.remove_least_frequent()
            del self.cache[least_frequent_node_key]
        else:
            self.size += 1
        
        self.add_new_node(new_node)
        self.cache[key] = new_node
        # print(self.cache)
        # print(self.head.next.value)
        # print(self.tail.prev.value)
        
    def remove_least_frequent(self):
        if self.head.next == self.tail:
            return
        next_node = self.head.next
        next_node.next.prev = self.head
        self.head.next = next_node.next
    
    def add_new_node(self, node):
        prev_node = self.tail.prev
        prev_node.next = node
        node.next = self.tail
        node.prev = prev_node
        self.tail.prev = node
    
    def move_to_end(self, node):
        # print('======= BEFORE ======')
        # print(self.head.next.value)
        # print(self.tail.prev.value)
        # print('=====================')
        node.prev.next = node.next
        node.next.prev = node.prev
        
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
