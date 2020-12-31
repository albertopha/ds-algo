class MergeSort():
    def __init__(self):
        return

    def merge_sort(self, arr):
        if len(arr) < 2:
            return arr

        half_point = len(arr) // 2
        left = self.merge_sort(arr[0:half_point])
        right = self.merge_sort(arr[half_point:])

        return self.merge(left, right)

    def merge(self, left, right):
        l, r, merged = 0, 0, []

        while l < len(left) and r < len(right):
            if left[l] == right[r]:
                merged.extend([left[l], left[l]])
                l += 1
                r += 1
            elif left[l] < right[r]:
                merged.append(left[l])
                l += 1
            else:
                merged.append(right[r])
                r += 1

        if l < len(left):
            merged.extend(left[l:])
        elif r < len(right):
            merged.extend(right[r:])

        return merged


if __name__ == '__main__':
    mergeSort = MergeSort()
    sorted = mergeSort.merge_sort([5, 4, 3, 2, 1, 0])
    sorted2 = mergeSort.merge_sort([5, 1, 6, 4, 2, 3])
    print(sorted)
    print(sorted2)