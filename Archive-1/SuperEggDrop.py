class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        res = [[0 for i in range(N + 1)] for j in range(K)]
        for i in range(N + 1):
            res[0][i] = i
        for k in range(1, K):
            i = 0
            for n in range(1, N + 1):
                while res[k - 1][i + 1] <= res[k][n - i - 2]:
                    i += 1
                res[k][n] = 1 + min(res[k][n - i - 1], res[k - 1][i + 1])
        # print(res[-1])
        return res[-1][-1]

    def superEggDrop1(self, K, N):
        drops = 0  # the number of eggs dropped
        floors = [
            0 for _ in range(K + 1)
        ]  # floors[i] is the number of floors that can be checked with i eggs

        while floors[K] < N:  # until we can reach N floors with K eggs

            for eggs in range(K, 0, -1):
                floors[eggs] += 1 + floors[eggs - 1]
            drops += 1

        return drops


if __name__ == '__main__':
    s = Solution()
    s.superEggDrop(4, 40)
    s.superEggDrop(4, 200)
