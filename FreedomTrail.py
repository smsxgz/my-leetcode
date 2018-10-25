from collections import defaultdict


class Solution:
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        cache = dict()

        def _solve(ring, key):
            if len(key) == 0:
                return 0
            if (ring, key) in cache:
                return cache[(ring, key)]

            ch = key[0]
            n = len(ring)
            min_step = 10000
            for idx, s in enumerate(ring):
                if s == ch:
                    min_step = min(
                        min_step,
                        min(idx, n - idx) + 1 + _solve(ring[idx:] + ring[:idx],
                                                       key[1:]))
            cache[(ring, key)] = min_step
            return min_step

        return _solve(ring, key)


if __name__ == '__main__':
    s = Solution()
    s.findRotateSteps("godding", 'gd')
