from QuickSort import QuickSort


#!
class SortedMerge:
    def __init__(self):
        return

    @staticmethod
    def sorted_merge_brute(A, B):
        y = 0
        for i in range(len(A)):
            if A[i] is None:
                A[i] = B[y]
                y += 1

        qs = QuickSort()
        qs.quick_sort(A)
        print(A)

    @staticmethod
    def sorted_merge_optimal(A, B):
        a, b, end = 0, len(B)-1, len(A)-1

        for i in range(len(A)):
            if A[i] is None:
                a = i-1
                break

        while b >= 0:
            if a >= 0 and A[a] >= B[b]:
                A[end] = A[a]
                a -= 1
            else:
                A[end] = B[b]
                b -= 1
            end -= 1

        print(A)


if __name__ == '__main__':
    sm = SortedMerge()
    sm.sorted_merge_brute([2, 5, 9, 11, None, None, None, None], [1, 3, 5, 8])
    sm.sorted_merge_optimal([2, 5, 9, 11, None, None, None, None], [1, 3, 5, 8])
    sm.sorted_merge_optimal([0, 5, 9, None, None, None, None], [1, 3, 5, 8])
    sm.sorted_merge_optimal([2, 5, 9, None, None, None], [1, 3, 5])



