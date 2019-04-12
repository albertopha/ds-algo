class QuickSort():
    def __init__(self):
        return

    def quick_sort(self, arr):
        if len(arr) < 2:
            return arr

        self.quick_sort_helper(arr, 0, len(arr)-1)

    def quick_sort_helper(self, arr, start, end):
        if start >= end:
            return

        s, e, p = start, end-1, end
        while s < e:

            while s < p and arr[s] < arr[p]:
                s += 1

            while e >= 0 and arr[e] > arr[p]:
                e -= 1

            if s > e:
                break

            arr[s], arr[e] = arr[e], arr[s]

        if arr[s] >= arr[p]:
            arr[p], arr[s] = arr[s], arr[p]
            self.quick_sort_helper(arr, start, s-1)
            self.quick_sort_helper(arr, s+1, end)


if __name__ == '__main__':
    quickSort = QuickSort()
    arr1 = [1, 2, 0]
    arr2 = [5, 1, 6, 4, 2, 3]
    arr3 = [5, 4]
    arr4 = [5, 4, 3, 2, 1, 0]

    quickSort.quick_sort(arr1)
    quickSort.quick_sort(arr2)
    quickSort.quick_sort(arr3)
    quickSort.quick_sort(arr4)

    print(arr1)
    print(arr2)
    print(arr3)
    print(arr4)
