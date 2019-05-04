#!
class Word:
    def __init__(self, ind, word):
        self.ind = ind
        self.word = word


class Groupanagrams:
    def __init__(self):
        return

    def group_anagrams_opt(self, arr):
        sorted_array = []
        word_lists = self.create_word_lists(arr)
        word_lists = sorted(word_lists, cmp=self.sort_by_opt)

        for i in range(len(word_lists)):
            sorted_array.append(arr[word_lists[i].ind])

        return sorted_array

    @staticmethod
    def create_word_lists(arr):
        list_of_words = []

        for i in range(len(arr)):
            curr = ''.join(sorted(arr[i]))
            list_of_words.append(Word(i, curr))

        return list_of_words

    @staticmethod
    def sort_by_opt(word1, word2):
        # Sort by length:
        if len(word1.word) != len(word2.word):
            return len(word1.word) - len(word2.word)

        if word1.word == word2.word:
            return 0
        if word1.word < word2.word:
            return -1
        return 1

    def group_anagrams_brute(self, arr):
        if len(arr) < 2:
            return arr

        return sorted(arr, cmp=self.sort_by)

    def sort_by(self, word1, word2):
        # Sort by length:
        if len(word1) != len(word2):
            return len(word1) - len(word2)

        # Not working:
        if self.equals(word1, word2):
            return -1
        else:
            return 1


    @staticmethod
    def equals(word1, word2):
        """
        Equal if they are anagrams
        :param word1: String
        :param word2: String
        :return: Boolean
        """

        hash_char = {}

        for i in range(len(word1)):
            curr = word1[i]

            if curr in hash_char:
                hash_char[curr] += 1
            else:
                hash_char[curr] = 1

        for i in range(len(word2)):
            curr = word2[i]

            if curr not in hash_char:
                return False
            elif hash_char[curr] == 0:
                return False
            else:
                hash_char[curr] -= 1

        return True


if __name__ == '__main__':
    ga = Groupanagrams()
    print(ga.group_anagrams_brute(['abc', 'ab', 'cba', 'cbb', 'bcb', 'ba', 'a', 'b', 'c', 'c', 'ba', 'bac']))
    print(ga.group_anagrams_opt(['abc', 'ab', 'cba', 'cbb', 'bcb', 'ba', 'a', 'b', 'c', 'c', 'ba', 'bac']))
