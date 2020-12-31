# https://leetcode.com/discuss/interview-question/356520
# https://www.geeksforgeeks.org/find-the-point-where-maximum-intervals-overlap/
# https://www.youtube.com/watch?v=GmpyAMpjpUY


class Solution(object):
    def find_min_num_of_chairs(self, S, E):
        if len(S) <= 1:
            return len(S)

        return self.brute_force(S, E)

    @staticmethod
    def brute_force(S, E):
        max_chair = 0
        # starting point:
        start_time = min(S)
        # end point:
        end_time = max(E)

        while start_time <= end_time:
            count = 0
            for i in range(len(S)):
                if S[i] <= start_time < E[i]:
                    count += 1

            print(count)

            max_chair = count if max_chair < count else max_chair
            start_time += 1

        return max_chair


if __name__ == '__main__':
    s = Solution()
    S, E = [1, 2, 6, 5, 3], [5, 5, 7, 6, 8]
    print(s.find_min_num_of_chairs(S, E))

    S, E = [1, 2, 9, 5, 5], [4, 5, 12, 9, 12]
    print(s.find_min_num_of_chairs(S, E))
