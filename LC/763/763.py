class Solution:
    def partitionLabels(self, S):
        result = []
        start = 0

        while start < len(S):
            current = S[start]
            current_end = start
            for end in range(len(S) - 1, start, -1):
                if current == S[end]:
                    current_end = end
                    break

            print('current_end ->', current_end)
            next_start = start + 1
            seen = dict()
            seen[current] = current_end
            while next_start < current_end:
                print('next_start = ', next_start)
                next_char = S[next_start]
                if next_char == current or next_char in seen:
                    next_start += 1
                    continue

                for end in range(len(S) - 1, current_end, -1):
                    if next_char == S[end]:
                        current_end = end
                        break
                print('inner: current_end -> ', current_end)
                seen[next_char] = current_end
                next_start += 1
            print('outer: current_end -> ', current_end)
            result.append([current_end - start + 1])
            start = current_end + 1
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.partitionLabels("ababcbacadefegdehijhklij"))
