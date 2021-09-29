"""
1. Sort by the timestamp (is it already sorted?)
2. UnionFind to operate union process while counting
3. Return the timestamp as soon as count equals to n - 1
"""

class UnionFind(object):

    def __init__(self, n: int):
        self.count = 0
        self.ranks = [0] * n
        self.sets = [i for i in range(n)]

    def getCount(self) -> int:
        return self.count

    def find(self, node: int) -> int:
        if self.sets[node] == node:
            return node
        self.sets[node] = self.find(self.sets[node])
        return self.sets[node]

    def union(self, node1: int, node2: int) -> None:
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 == root2:
            return

        self.count += 1

        if self.ranks[root1] > self.ranks[root2]:
            self.sets[root2] = root1
        elif self.ranks[root1] < self.ranks[root2]:
            self.sets[root1] = root2
        else:
            self.sets[root2] = root1
            self.ranks[root1]+=1


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        if not logs or n == 0:
            return -1

        logs.sort(key=lambda log: log[0])
        
        uf = UnionFind(n)
        for timestamp, source, target in logs:
            uf.union(source, target)
            count = uf.getCount()

            print(source, target, count)

            if count == n-1:
                return timestamp

        return -1