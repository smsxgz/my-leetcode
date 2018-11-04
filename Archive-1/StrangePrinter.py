class Solution:
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        cache = dict()

        def _solve(i, j, k):
            ch = s[i]
            while i < j - 1 and s[i + 1] == ch:
                i += 1
                k += 1

            if j - i == 1:
                return 1

            if (i, j, k) in cache:
                return cache[(i, j, k)]

            temp = 1 + _solve(i + 1, j, 0)
            for ii in range(i + 2, j):
                if s[ii] == ch:
                    temp = min(temp,
                               _solve(i + 1, ii, 0) + _solve(ii, j, k + 1))

            cache[(i, j, k)] = temp
            return temp

        return _solve(0, len(s), 0)


if __name__ == '__main__':
    s = Solution()
    s.strangePrinter('aaabbb')
    s.strangePrinter('aba')
