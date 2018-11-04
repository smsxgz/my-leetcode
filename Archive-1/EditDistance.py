class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word1) > len(word2):
            word1, word2 = word2, word1

        if len(word1) == 0:
            return len(word2)

        m = len(word1)
        n = len(word2)

        res = [[0 for i in range(n)] for j in range(m)]

        res[0][0] = int(word1[0] != word2[0])
        for i in range(1, n):
            if word1[0] == word2[i]:
                res[0][i] = i
            else:
                res[0][i] = 1 + res[0][i - 1]

        for i in range(1, m):
            if word1[i] == word2[0]:
                res[i][0] = i
            else:
                res[i][0] = 1 + res[i - 1][0]

        for j in range(1, m):
            for i in range(1, n):
                if word1[j] == word2[i]:
                    res[j][i] = res[j - 1][i - 1]
                else:
                    res[j][i] = 1 + min(res[j][i - 1], res[j - 1][i - 1],
                                        res[j - 1][i])

        # print(res)
        return res[-1][-1]


if __name__ == '__main__':
    s = Solution()
    s.minDistance("intention", "execution")
    s.minDistance("plasma", "altruism")
