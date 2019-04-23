class RecursiveMultiply:
    def __init__(self):
        return

    def recursive_multiply_brute_force(self, a, b, total=0):
        if b == 0:
            return total

        return self.recursive_multiply_brute_force(a, b-1, total+a)


if __name__ == '__main__':
    rm = RecursiveMultiply()
    print(rm.recursive_multiply_brute_force(0, 6))
    print(rm.recursive_multiply_brute_force(1, 6))
    print(rm.recursive_multiply_brute_force(2, 7))
    print(rm.recursive_multiply_brute_force(3, 8))
