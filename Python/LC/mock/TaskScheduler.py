import functools
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Best Answer:
        counter = list(collections.Counter(tasks).values())
                maxx = max(counter)
                numOfMax = counter.count(maxx)
                return max(len(tasks), (maxx - 1) * (n + 1) + numOfMax)
        """
        if tasks is None or len(tasks) == 0:
            return 0

        if n == 0:
            return len(tasks)

        kinds = {}

        for task in tasks:
            if task in kinds:
                kinds[task] += 1
            else:
                kinds[task] = 1

        kinds_n = len(kinds)
        max_value = max(value for value in kinds.values())
        count_max_values = functools.reduce(lambda count, value: count + 1 if value == max_value else count,
                                            kinds.values(), 0) - 1

        if kinds_n - 1 > n:
            return max(len(tasks), n * (max_value - 1) + max_value)
        else:
            return n * (max_value - 1) + max_value + count_max_values

