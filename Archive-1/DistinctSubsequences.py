class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if not s and t:
            return 0

        dp = [[0 for _1 in range(len(s))] for _2 in range(len(t))]

        if s[0] == t[0]:
            dp[0][0] = 1

        for j in range(1, len(s)):
            dp[0][j] = dp[0][j - 1]
            if s[j] == t[0]:
                dp[0][j] += 1

        for i in range(1, len(t)):
            for j in range(1, len(s)):
                dp[i][j] = dp[i][j - 1]
                if s[j] == t[i]:
                    dp[i][j] += dp[i - 1][j - 1]

        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    s.numDistinct("babgbag", "bag")
