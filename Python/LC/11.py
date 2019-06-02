class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return 0

        start = 0
        end = len(height) - 1
        area = 0

        while start < end:
            area = max((end - start) * min(height[start], height[end]), area)
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        return area


if __name__ == '__main__':
    ma = Solution()
    print(ma.maxArea([1, 2, 4, 3]))
    print(ma.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
