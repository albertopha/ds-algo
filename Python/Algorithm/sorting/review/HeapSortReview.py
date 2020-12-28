class Heap(object):
  def __init__(self):
    return

  def heapify(self, arr):
    if not arr:
      return arr

    for i in range(1, len(arr)):
      ci = i
      while ci > 0:
        pi = (ci - 1) // 2

        if arr[pi] <= arr[ci]:
          break

        arr[pi], arr[ci] = arr[ci], arr[pi]
        ci = pi
    print(arr)

  def heap_pop(self, heap):
    if not heap:
      return

    # Make the lowest element root
    heap[0], heap[-1] = heap[-1], heap[0]
    popped = heap.pop(-1)
    
    i = 0
    while i < len(heap):
      first_child_ind = 2 * i + 1
      second_child_ind = 2 * i + 2

      if first_child_ind >= len(heap):
        return popped

      min_child_ind = first_child_ind

      if second_child_ind < len(heap) and heap[second_child_ind] < heap[min_child_ind]:
        min_child_ind = second_child_ind

      if heap[min_child_ind] >= heap[i]:
        return popped

      heap[i], heap[min_child_ind] = heap[min_child_ind], heap[i]
      i = min_child_ind
    return popped

  def heap_push(self, heap, val):
    if not heap:
      return

    heap.append(val)
    ci = len(heap) - 1
    while ci >= 0:
      pi = (ci - 1) // 2

      if heap[pi] <= heap[ci]:
        break

      heap[pi], heap[ci] = heap[ci], heap[pi]
      ci = pi

  def heap_sort(self, arr):
    if not arr:
      return

    self.heapify(arr)
    sorted_list = []

    while arr:
      popped = self.heap_pop(arr)
      sorted_list.append(popped)

    return sorted_list


if __name__ == "__main__":
  heap = Heap()
  print(heap.heap_sort([10,4,2,2,0,0,1,3,8,6,7,9]))
  print(heap.heap_sort([0,1]))
  print(heap.heap_sort([1,2]))
  print(heap.heap_sort([0,0,0,0,0,0,0,0,0]))
  print(heap.heap_sort([0]))
