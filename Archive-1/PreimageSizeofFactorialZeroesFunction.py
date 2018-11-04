class Solution(object):
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        n = m = (4 * K + 4) // 5 * 5
        s = 0
        log5 = 0
        while m >= 5:
            m //= 5
            s += m
            log5 += 1

        if s == K:
            return 5
        elif log5 < 2:
            return 0

        pows = [25]
        for _ in range(3, log5 + 1):
            pows.append(pows[-1] * 5)

        for d in range(5, 4 * log5 + 1, 5):
            s += 1
            for p in pows:
                if (n + d) % p == 0:
                    s += 1
                else:
                    break
            if s == K:
                return 5
            elif s > K:
                return 0


if __name__ == '__main__':
    s = Solution()
    s.preimageSizeFZF(5)
