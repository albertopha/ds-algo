class DC1(object):
    @staticmethod
    def dc1_opt(arr, k):
        hash_map = {}

        for i in range(len(arr)):
            curr = arr[i]

            if curr in hash_map:
                return True

            hash_map[k-curr] = True

        return False


if __name__ == '__main__':
    dc1 = DC1()
    print(dc1.dc1_opt([10, 15, 3, 7], 17))
    print(dc1.dc1_opt([10, 15, 3, 7], 11))
