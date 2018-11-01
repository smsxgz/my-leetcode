class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        cache = dict()
        n = len(s)
        idx = n - 1
        cache[idx] = [n - 1]

        while idx > 0:
            idx -= 1
            ch = s[idx]
            tmp = [idx, idx + 1]
            for i in cache[idx + 1]:
                if i < n and ch == s[i]:
                    tmp.append(i + 1)
            cache[idx] = tmp

        res = dict()

        def _solve(i):
            if i == n - 1:
                return 0

            if i in res:
                return res[i]

            ans = n - i
            for j in cache[i][:0:-1]:
                if j == n:
                    ans = 0
                    break

                ans = min(ans, 1 + _solve(j))

            res[i] = ans
            return ans

        return _solve(0)

    def minCut1(self, s):
        if s == s[::-1]:
            return 0

        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1

        # algorithm
        cut = [x for x in range(-1, len(s))]
        for i in range(len(s)):
            r1, r2 = 0, 0
            # use i as origin, and gradually enlarge radius if a palindrome
            # exists odd palindrome
            while i - r1 >= 0 and i + r1 < len(s) and s[i - r1] == s[i + r1]:
                cut[i + r1 + 1] = min(cut[i + r1 + 1], cut[i - r1] + 1)
                r1 += 1
            # even palindrome
            while i - r2 >= 0 and i + r2 + 1 < len(s) and s[i - r2] == s[i + r2
                                                                         + 1]:
                cut[i + r2 + 2] = min(cut[i + r2 + 2], cut[i - r2] + 1)
                r2 += 1
        return cut[-1]


if __name__ == '__main__':
    s = Solution()
    s.minCut('aab')
    s.minCut('abba')
