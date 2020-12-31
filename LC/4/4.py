class MedianTwoSortedArr(object):
    def median_two_sorted_arr_brute(self, nums1, nums2):
        merged_arr = self.merge(nums1, nums2)
        sum_len = len(nums1) + len(nums2)
        median = sum_len/2

        if sum_len % 2 == 0:
            return (float(merged_arr[median-1]) + float(merged_arr[median]))/2
        else:
            return float(merged_arr[median])

    @staticmethod
    def merge(nums1, nums2):
        arr = []
        n1, n2 = 0, 0

        while n1 < len(nums1) and n2 < len(nums2):
            if nums1[n1] <= nums2[n2]:
                arr.append(nums1[n1])
                n1 += 1
            else:
                arr.append(nums2[n2])
                n2 += 1

        if n1 < len(nums1):
            arr.extend(nums1[n1:])

        if n2 < len(nums2):
            arr.extend(nums2[n2:])

        return arr


if __name__ == '__main__':
    mtsa = MedianTwoSortedArr()
    print(mtsa.median_two_sorted_arr_brute([1, 3], [2]))
    print(mtsa.median_two_sorted_arr_brute([1, 2], [3, 4]))
    print(mtsa.median_two_sorted_arr_brute([], [2, 3]))

