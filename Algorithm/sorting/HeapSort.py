class HeapSort():
    def __init__(self):
        return

    def heap_sort(self, arr):
        if len(arr) < 2:
            return arr

        result = []
        first_parent = (len(arr)-1) / 2
        # Heapify starting from end of the array:
        for root in range(first_parent, -1, -1):
            self.heapify(arr, root)

        # Replace root with end of the array and re-heapify:
        while len(arr) != 0:
            result.append(arr[0])
            arr[0] = arr[len(arr)-1]
            arr = arr[0:len(arr)-1]
            self.heapify(arr, 0)

        return result

    def heapify(self, arr, root):
        left = root * 2 + 1
        right = root * 2 + 2
        min_root = root

        if left < len(arr) and arr[min_root] > arr[left]:
            min_root = left

        if right < len(arr) and arr[min_root] > arr[right]:
            min_root = right

        if min_root != root:
            arr[min_root], arr[root] = arr[root], arr[min_root]
            self.heapify(arr, min_root)


if __name__ == "__main__":
    heapSort = HeapSort()
    a1 = [5, 4, 3, 2, 1, 0]
    a2 = [5, 1, 6, 4, 2, 3]
    a3 = [2, 0, 1]

    hs1 = heapSort.heap_sort(a1)
    hs2 = heapSort.heap_sort(a2)
    hs3 = heapSort.heap_sort(a3)

    print(hs1)
    print(hs2)
    print(hs3)
