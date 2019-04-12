class SelectionSort():
    def __init__(self):
        return

    def selection_sort(self, arr):

        for i in range(len(arr)-1):
            find_min = arr[i]
            min_index = i
            for j in range(i+1, len(arr)):
                if arr[j] < find_min:
                    find_min = arr[j]
                    min_index = j

            self.swap(arr, i, min_index)

        print(arr)

    @staticmethod
    def swap(arr, i, j):
        temp = arr[j]
        arr[j] = arr[i]
        arr[i] = temp


if __name__ == '__main__':
    selectionSort = SelectionSort()
    selectionSort.selection_sort([5, 4, 3, 2, 1, 0])
    selectionSort.selection_sort([5, 1, 6, 3, 2, 4])
