from PermutationNoDup import PermutationNoDup


class PermutationWithDup:
    def __init__(self):
        return

    @staticmethod
    def permutation_with_dup_brute(s):
        pnd = PermutationNoDup()
        return pnd.permutation_without_dup(s)


if __name__ == '__main__':
    pwd = PermutationWithDup()
    perm1 = pwd.permutation_with_dup_brute('aba')
    print(perm1)