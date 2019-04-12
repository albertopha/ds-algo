class QuickSort():
    def __init__(self):
        return

    def quick_sort(self, arr):
        if len(arr) < 2:
            return arr

        self.quick_sort_helper(arr, 0, len(arr)-1)

    def quick_sort_helper(self, arr, start, end):
        if end - start < 2:
            if arr[start] > arr[end]:
                self.swap(arr, start, end)
            return

        print(arr[start:end+1])

        # Get Pivot value:
        pivot = (start + end) // 2

        # Move pivot to last element:
        self.swap(arr, pivot, end)

        from_left = start
        from_right = end - 1

        # iterate from_left and from_right:
        while from_left < from_right:

            # Find element higher than pivot value
            while arr[from_left] < arr[end] and from_left < end:
                from_left += 1

            # Find element less than pivot value
            while arr[from_right] > arr[end] and from_right > start:
                from_right -= 1

            # Double-check if from_left isn't higher than the from_right
            if from_left >= from_right:
                break

            self.swap(arr, from_left, from_right)

        print(arr)
        # Swap from_left and pivotted value
        if from_left <= end:
            self.swap(arr, from_left, end)
            print(from_left)
            self.quick_sort_helper(arr, start, from_left-1)
            self.quick_sort_helper(arr, from_left+1, end)

    @staticmethod
    def swap(arr, l, r):
        temp = arr[l]
        arr[l] = arr[r]
        arr[r] = temp


if __name__ == '__main__':
    quickSort = QuickSort()
    arr1 = [1,2,0]
    arr2 = [5, 1, 6, 4, 2, 3]
    arr3 = [5, 4]
    arr4 = [5, 4, 3, 2, 1]

    quickSort.quick_sort(arr1)
    # quickSort.quick_sort(arr2)
    # quickSort.quick_sort(arr3)
    # quickSort.quick_sort(arr4)

    print(arr1)
    # print(arr2)
    # print(arr3)
    # print(arr4)
