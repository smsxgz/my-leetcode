# def is_palindrome(s):
#     n = len(s)
#     if n == 1:
#         return True
#
#     m = n // 2
#     return s[:m] == s[:n - m - 1:-1]
#


class Solution(object):
    def partition(self, s):
        """
        all possible palindrome partitioning
        :type s: str
        :rtype: List[List[str]]
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
            if i == n:
                return [[]]

            if i == n - 1:
                return [[s[i]]]

            if i in res:
                return res[i]

            ans = []
            for j in cache[i][1:]:
                for ll in _solve(j):
                    ans.append([s[i:j]] + ll)

            res[i] = ans
            return ans

        return _solve(0)

    def partition1(self, s):
        if not s:
            return []
        results = [[s[0]]]
        for indx in range(1, len(s)):
            nextResults = []
            for result in results:
                nextResults.append(result + [s[indx]])
                if result[-1] == s[indx]:
                    nextResults.append(result[:-1] + [result[-1] + s[indx]])
                if len(result) > 1 and result[-2] == s[indx]:
                    nextResults.append(result[:-2] +
                                       [result[-2] + result[-1] + s[indx]])
            results = nextResults
        return results


if __name__ == '__main__':
    s = Solution()
    s.partition1('aa')
    s.partition1('aaa')
    s.partition1('aaaa')
