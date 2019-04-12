class BubbleSort():
    def __init__(self):
        return None

    def bubble_sort(self, arr):
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                first = arr[i]
                second = arr[j]

                if first > second:
                    self.swap(arr, i, j)
        print(arr)

    @staticmethod
    def swap(arr, i, j):
        temp = arr[j]
        arr[j] = arr[i]
        arr[i] = temp


if __name__ == '__main__':
    bubbleSort = BubbleSort()
    bubbleSort.bubble_sort([5, 4, 3, 2, 1, 1, 1])
    bubbleSort.bubble_sort([5, 1, 6, 2, 4, 3])
