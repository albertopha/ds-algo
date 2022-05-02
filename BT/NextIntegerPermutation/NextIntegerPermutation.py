from collections import deque

class Solution:
    def solve(self, n):
        if n == 0:
            return 0
        
        l = self.intToList(n)
        drop_point = self.getDropPoint(l)

        if drop_point < 0:
            l.reverse()
            return self.listToInt(l)
        
        swap_point = self.getSwapPoint(l, drop_point)
        l[swap_point], l[drop_point] = l[drop_point], l[swap_point]
        self.reverseListRange(l, drop_point+1, len(l)-1)
        return self.listToInt(l)

    def reverseListRange(self, l, start, end):
        while start < end:
            l[start],l[end] = l[end],l[start]
            start+=1
            end-=1

    def getSwapPoint(self, l, start):
        point = start
        for i in range(start+1, len(l)):
            if l[i] <= l[start]:
                break
            point = i
        return point

    def getDropPoint(self, l):
        i = len(l)-2
        while i >= 0:
            if l[i] < l[i+1]:
                return i
            i -= 1
        return -1
    
    def listToInt(self, l):
        if not l:
            return 0
        
        num = 0
        while l:
            num *= 10
            num += l.popleft()
        return num
        
    def intToList(self, n):
        l = deque()
        while n > 0:
            l.appendleft(n % 10)
            n //= 10
        return l
