class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        cache = dict()
        if len(s3) != len(s1) + len(s2):
            return False

        def _solve(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            if i == 0:
                flag = s2[:j] == s3[:j]
                cache[(i, j)] = flag
                return flag
            elif j == 0:
                flag = s1[:i] == s3[:i]
                cache[(i, j)] = flag
                return flag

            flag = False
            ch = s3[i + j - 1]
            if ch == s1[i - 1] and _solve(i - 1, j):
                flag = True
            elif ch == s2[j - 1] and _solve(i, j - 1):
                flag = True

            cache[(i, j)] = flag
            return flag

        res = _solve(len(s1), len(s2))
        return res


if __name__ == '__main__':
    s = Solution()
    s.isInterleave("aabcc", "dbbca", "aadbbcbcac")
    s.isInterleave("aabcc", "dbbca", "aadbbbaccc")
