class Solution:
    def numPermsDISequence(self, S):
        """
        :type S: str
        :rtype: int
        """
        N = 10**9 + 7
        n = len(S) + 1
        dp = [0 for i in range(n)]

        dp[0] = 1
        for i in range(1, n):
            ch = S[i - 1]
            if ch == 'I':
                temp = [0 for i in range(n)]
                for j in range(1, i + 1):
                    temp[j] = temp[j - 1] + dp[j - 1]
                    temp[j] %= N
            else:
                temp = [0 for i in range(n)]
                for j in range(i - 1, -1, -1):
                    temp[j] = temp[j + 1] + dp[j]
                    temp[j] %= N

            dp = temp
            print(dp)
        return sum(dp) % N


if __name__ == '__main__':
    s = Solution()
    s.numPermsDISequence("DID")
