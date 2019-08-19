import re


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        result = ["", 0]
        result_dict = {}
        # words list:
        words = paragraph.split(' ')
        # banned hashmap:
        banned_dict = {ban: True for ban in banned}

        # Remove punctuations:
        for i in range(len(words)):
            words[i] = re.sub(r'[^\w\s]','',words[i])

        for word in words:
            curr = word.lower()
            if curr in banned_dict:
                continue

            if curr in result_dict:
                result_dict[curr] += 1
            else:
                result_dict[curr] = 1

        for word, count in result_dict.items():
            if result[1] < count:
                result[0] = word
                result[1] = count

        return result[0]


if __name__ == '__main__':
    s = Solution()
    print(s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
    print(s.mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]))
