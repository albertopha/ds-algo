"""
[1,2,2,2,3,5]
           ^
[2,2,5,6,3]
     ^
           ^

"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums1 or not nums2:
            return nums1
        
        i = ns1 = ns2 = 0
        ne2 = n
        
        for i in range(m+n):
            num1 = nums1[ns1] if ns1 < m else sys.maxsize
            num2 = nums2[ns2] if ns2 < n else sys.maxsize
            num3 = nums2[ne2] if ne2 < len(nums2) else sys.maxsize
            
            min_val = min(num1, num2, num3)
            if min_val == num1:
                ns1 += 1
                continue
                
            if min_val == num2:
                if ns1 < m:
                    nums2.append(nums1[ns1])
                nums1[ns1] = nums2[ns2]
                ns2 += 1
                ns1 += 1
                continue
                
            if ns1 < m:
                nums2.append(nums1[ns1])
            nums1[ns1] = num3
            ne2 += 1
            ns1 += 1
