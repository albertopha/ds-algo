class InsertionSort():
    def __init__(self):
        return

    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            j = i-1
            curr = arr[i]

            while j >= 0 and arr[j] > curr:
                arr[j+1] = arr[j]
                j -= 1

            arr[j+1] = curr

        print(arr)


if __name__ == '__main__':
    insertionSort = InsertionSort()
    insertionSort.insertion_sort([5, 4, 3, 2, 1, 0])
    insertionSort.insertion_sort([5, 1, 6, 4, 2, 3])
