class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        nums_index = [(nums[i], i) for i in range(len(nums))]
        counts = [0] * len(nums)
        self.mergeSort(nums_index, counts)
        return counts
    
    def mergeSort(self, nums: List[tuple[int, int]], counts: List[int]) -> List[tuple]:
        if len(nums) <= 1:
            return nums
        
        mid_point = len(nums) // 2
        left = self.mergeSort(nums[:mid_point], counts)
        right = self.mergeSort(nums[mid_point:], counts)
        return self.merge(left, right, counts)
    
    def merge(self, left: List[tuple], right: List[tuple], counts: List[int]) -> List[tuple]:
        sorted_list = []
        i, j = 0, 0
        lower_val_from_right_sub_array_count = 0
        while i < len(left) or j < len(right):
            left_num = left[i][0] if i < len(left) else sys.maxsize
            right_num = right[j][0] if j < len(right) else sys.maxsize
            
            if left_num <= right_num:
                sorted_list.append(left[i])
                counts[left[i][1]] += lower_val_from_right_sub_array_count
                i += 1
            else:
                sorted_list.append(right[j])
                lower_val_from_right_sub_array_count += 1
                j += 1
        return sorted_list
            
                
