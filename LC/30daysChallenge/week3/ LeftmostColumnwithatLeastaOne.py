# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        
        start = 0
        end = cols
        result = -1
        
        while start < end:
          mid = (start+end)//2
          
          foundOne = False
          for i in range(rows):
            if binaryMatrix.get(i, mid) == 1:
              foundOne = True
              break
          
          if foundOne:
            result = mid
            end = mid
          else:
            start = mid+1
        
        return result
