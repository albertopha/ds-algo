#!
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return True

        if len(board) == 0:
            return False

        b = self.exist_brute(board, word)
        return b

    def exist_brute(self, board, word):

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[0] \
                        and self.validate(board, word, row, col, 0):
                    return True

        return False

    def validate(self, board, word, row, col, word_ind):
        if len(word) == word_ind:
            return True

        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return False

        if word[word_ind] != board[row][col]:
            return False

        tmp = board[row][col]
        board[row][col] = '#'
        validates = self.validate(board, word, row, col - 1, word_ind + 1) \
            or self.validate(board, word, row, col + 1, word_ind + 1) \
            or self.validate(board, word, row - 1, col, word_ind + 1) \
            or self.validate(board, word, row + 1, col, word_ind + 1)
        board[row][col] = tmp

        return validates


if __name__ == '__main__':
    s = Solution()
    board = [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]

    print(s.exist(board[:], 'ABCCED'))
    print(s.exist(board[:], 'SEE'))
    print(s.exist(board[:], 'ABCB'))
