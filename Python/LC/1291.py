class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        return self.generate_sequence(low)

    def generate_sequence(self, num):
        count_digit = 1
        first_digit = num

        while first_digit > 1:
            first_digit //= 10
            count_digit += 1

        print('first_digit = ', first_digit)
        print('count_digit = ', count_digit)

        tens = 10 * (count_digit - 1)
        while tens > 0:

            tens //= 10

        current = 0
        while count_digit > 0:
            current = current * 10 + first_digit
            first_digit += 1
            count_digit -= 1

        return current


if __name__ == '__main__':
    s = Solution()
    print(s.sequentialDigits(10, 100))
    print(s.sequentialDigits(15, 100))
