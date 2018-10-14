DIGITS = set('123456789')


def get_valid_digits(board, i, j):
    s = set(board[i]) | set(board[k][j] for k in range(9))
    i_, j_ = i // 3 * 3, j // 3 * 3
    for _i in range(i_, i_ + 3):
        for _j in range(j_, j_ + 3):
            s.add(board[_i][_j])
    return (DIGITS - s)


class Solution(object):
    def solveSudoku1(self, board, i=0, j=0):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if i == 8 and j == 8:
            if board[i][j] == '.':
                s = get_valid_digits(board, i, j)
                if len(s) == 1:
                    board[i][j] = list(s)[0]
                    return True
                else:
                    return False
            return True

        _i, _j = i, j
        _j += 1
        if _j == 9:
            _j = 0
            _i += 1
        if board[i][j] == '.':
            s = get_valid_digits(board, i, j)
            for d in s:
                board[i][j] = d
                if self.solveSudoku1(board, _i, _j):
                    return True
                board[i][j] = '.'
            return False
        else:
            return self.solveSudoku1(board, _i, _j)

    def solveSudoku(self, board):
        self.board = board
        self.val = self.PossibleVals()
        self.Solver()

    def PossibleVals(self):
        nrows = len(self.board)
        ncols = len(self.board[0])
        digits = "123456789"
        val = {}
        d = {}
        for r in range(nrows):
            for c in range(ncols):
                if self.board[r][c] == ".":
                    val[(r, c)] = []
                else:
                    d[("r", r)] = d.get(("r", r), []) + [self.board[r][c]]
                    d[("c", c)] = d.get(("c", c), []) + [self.board[r][c]]
                    d[(r // 3, c // 3)] = d.get(
                        (r // 3, c // 3), []) + [self.board[r][c]]
        for k in val.keys():
            occupied = d.get((k[0] // 3, k[1] // 3), []) + d.get(
                ("r", k[0]), []) + d.get(("c", k[1]), [])
            val[k] = [n for n in digits if n not in occupied]
        return val

    def Solver(self):
        if len(self.val) == 0:
            return True
        sKey = min(self.val.keys(), key=lambda key: len(self.val[key]))
        nums = self.val[sKey]
        for n in nums:
            update = {sKey: self.val[sKey]}
            if self.validOneCell(n, sKey, update):
                if self.Solver():
                    return True
            self.undo(sKey, update)
        return False

    def validOneCell(self, n, sKey, update):
        self.board[sKey[0]][sKey[1]] = n
        del self.val[sKey]
        (r, c) = sKey
        for k in self.val.keys():
            if n in self.val[k]:
                if r == k[0] or c == k[1] or (r // 3 == k[0] // 3
                                              and c // 3 == k[1] // 3):
                    update[k] = n
                    self.val[k].remove(n)
                    if len(self.val[k]) == 0:
                        return False
        return True

    def undo(self, sKey, update):
        self.board[sKey[0]][sKey[1]] = "."
        for k in update.keys():
            if k not in self.val:
                self.val[k] = update[k]
            else:
                self.val[k].append(update[k])


if __name__ == '__main__':
    board = [
        [".", ".", "9", "7", "4", "8", ".", ".", "."],
        ["7", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", "2", ".", "1", ".", "9", ".", ".", "."],
        [".", ".", "7", ".", ".", ".", "2", "4", "."],
        [".", "6", "4", ".", "1", ".", "5", "9", "."],
        [".", "9", "8", ".", ".", ".", "3", ".", "."],
        [".", ".", ".", "8", ".", "3", ".", "2", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "6"],
        [".", ".", ".", "2", "7", "5", "9", ".", "."],
    ]
    s = Solution()
    s.solveSudoku(board)
