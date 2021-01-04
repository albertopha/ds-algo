#####################################################
#
# Given an array, find the average of all contiguous
# subarrays of size ‘K’ in it.
#
#####################################################
import sys
def findMaxAverage(nums, k):
    if not nums:
        return 0

    max_avg = -sys.maxsize
    curr_sum = 0
    left = 0
    for right in range(len(nums)):
        curr_sum += nums[right]
        if right >= k - 1:
            max_avg = max(max_avg, curr_sum / k)
            curr_sum -= nums[left]
            left += 1

    return max_avg


if __name__ == "__main__":
    arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    k = 5
    print(findMaxAverage(arr, k))

