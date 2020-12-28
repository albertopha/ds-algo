class QuickSort(object):
  def __init__(self):
    return

  def quick_sort(self, arr, start, end):
    if not arr:
      return

    if start >= end:
      return

    partitioned_ind = self.partition(arr, start, end)
    self.quick_sort(arr, start, partitioned_ind-1)
    self.quick_sort(arr, partitioned_ind+1, end)

  def partition(self, arr, start, end):
    smaller_ind = start - 1
    pivot = arr[end]

    for i in range(start, end):
      if arr[i] < pivot:
        smaller_ind += 1
        arr[i], arr[smaller_ind] = arr[smaller_ind], arr[i]

    arr[smaller_ind+1], arr[end] = arr[end], arr[smaller_ind+1]
    return smaller_ind+1


if __name__ == "__main__":
 qs = QuickSort()
 
 arr = [5,2,1,4,3,0,1]
 qs.quick_sort(arr, 0, len(arr)-1)
 print(arr)
