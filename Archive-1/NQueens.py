class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        grid = [0 for i in range(n) for j in range(n)]
        res = 0
        for g in _solve(grid, 0, n):
            res += 1
        return res


def _solve(grid, start_row, n):
    if start_row == n - 1:
        for j in range(n):
            if grid[start_row * n + j] == 0:
                grid[start_row * n + j] = 1
                yield grid
                return

    for j in range(n):
        if grid[start_row * n + j] == 0:
            tmp_grid = grid.copy()
            tmp_grid[start_row * n + j] = 1
            for i in range(1, min(n - j, n - start_row)):
                tmp_grid[(start_row + i) * n + j + i] = -1
            for i in range(1, min(j + 1, n - start_row)):
                tmp_grid[(start_row + i) * n + j - i] = -1
            for i in range(1, n - start_row):
                tmp_grid[(start_row + i) * n + j] = -1
            yield from _solve(tmp_grid, start_row + 1, n)


if __name__ == '__main__':
    s = Solution()
    s.solveNQueens(4)
