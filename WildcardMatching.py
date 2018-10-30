class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[0 for _1 in range(len(s) + 1)] for _2 in range(len(p) + 1)]

        dp[0][0] = 1
        for i, ch in enumerate(p):
            if ch != '*':
                break
            dp[i + 1][0] = 1

        for i in range(1, len(p) + 1):
            ch = p[i - 1]
            if ch == '*':
                flag = dp[i - 1][0]
                for j in range(1, len(s) + 1):
                    if dp[i - 1][j]:
                        flag = 1
                    dp[i][j] = flag
            else:
                for j in range(1, len(s) + 1):
                    if p[i - 1] == s[j - 1] or p[i - 1] == '?':
                        dp[i][j] = dp[i - 1][j - 1]

        return dp[-1][-1] == 1

    def isMatch1(self, s, p):
        if p == "" and s:
            return False

        starIdx = -1
        match = 0
        i, j = 0, 0

        len_s = len(s)
        len_p = len(p)

        while i < len_s:
            if j < len_p and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif j < len_p and p[j] == '*':
                starIdx = j
                match = i
                j += 1
            elif starIdx != -1:
                match += 1
                i = match
                j = starIdx + 1
            else:
                return False

        while j < len_p:
            if p[j] != "*":
                return False
            j += 1
        return True


if __name__ == '__main__':
    s = Solution()
    s.isMatch("a", "a****")
    s.isMatch("adceb", "*a*b")
