class PowerSet:
    def __init__(self):
        return

    def get_power_set(self, arr):
        power_sets = []

        if len(arr) == 0:
            return power_sets

        self.get_power_set_brute_force(arr, power_sets)
        power_sets.append([])
        return power_sets

    def get_power_set_brute_force(self, arr, power_sets):
        if len(arr) == 0:
            return

        if arr not in power_sets:
            power_sets.append(arr)

        for skip_index in range(len(arr)):
            if skip_index == 0:
                self.get_power_set_brute_force(arr[1:], power_sets)
            elif skip_index == len(arr)-1:
                self.get_power_set_brute_force(arr[0:len(arr)-1], power_sets)
            else:
                self.get_power_set_brute_force(arr[skip_index:len(arr)-1], power_sets)


if __name__ == '__main__':
    ps = PowerSet()

    print(ps.get_power_set([]))
    print(ps.get_power_set([1]))
    print(ps.get_power_set([1, 2]))
    print(ps.get_power_set([1, 2, 3]))
    print(ps.get_power_set([1, 2, 3, 4]))
