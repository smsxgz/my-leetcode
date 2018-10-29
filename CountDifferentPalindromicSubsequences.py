class Solution:
    def countPalindromicSubsequences(self, S):
        """
        :type S: str
        :rtype: int
        """
        cache = dict()
        M = 10**9 + 7

        def _solve(string):
            if string in cache:
                return cache[string]

            res = 0
            for ch in 'abcd':
                try:
                    i = string.index(ch)
                    j = string.rindex(ch)
                    if i == j:
                        res += 1
                    else:
                        res += 2 + _solve(string[i + 1:j])

                except Exception:
                    continue

            res %= M
            cache[string] = res
            return res

        return _solve(S)


if __name__ == '__main__':
    s = Solution()
    s.countPalindromicSubsequences(
        'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba')
