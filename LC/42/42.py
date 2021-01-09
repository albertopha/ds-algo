#! re - Stack and 2 pointers
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if len(height) < 2:
            return 0

        return self.optimized_dp(height)

    def brute_force(self, height):
        total_water = 0

        for i in range(len(height)):
            lmax, rmax = 0, 0
            for l in range(i-1, -1, -1):
                lmax = max(height[l], lmax)
            for r in range(i+1, len(height)):
                rmax = max(height[r], rmax)

            curr_water = min(lmax, rmax) - height[i]
            total_water += 0 if curr_water < 0 else curr_water

        return total_water

    def optimized_dp(self, height):
        total_water = 0
        lmax_list, rmax_list = [0] * len(height), [0] * len(height)
        lmax, rmax = height[0], height[len(height)-1]

        for l in range(1, len(height)):
            lmax = max(lmax, height[l])
            lmax_list[l] = lmax

        for r in range(len(height)-2, -1, -1):
            rmax = max(rmax, height[r])
            rmax_list[r] = rmax

        for i in range(len(height)):
            curr_water = min(lmax_list[i], rmax_list[i]) - height[i]
            total_water += 0 if curr_water < 0 else curr_water

        return total_water

    def lowerEnvelop(self, height):
        """
        Using two pointers
        https://www.youtube.com/watch?v=XqTBrQYYUcc&t=4s
        
        T: O(N)
        S: O(1)
        """
        i, j = 0, len(height) - 1
        left_max, right_max = 0, 0
        
        rain = 0
        while i < j:
            if height[i] <= height[j]:
                left_max = max(left_max, height[i])
                rain += left_max - height[i]
                i += 1
            else:
                right_max = max(right_max, height[j])
                rain += right_max - height[j]
                j -= 1
        
        return rain

if __name__ == '__main__':
    s = Solution()
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(s.trap([1, 2]))
    print(s.trap([2, 1]))
    print(s.trap([3, 1, 2, 1]))
