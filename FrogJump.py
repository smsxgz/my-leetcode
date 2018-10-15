class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """

        visited = set()
        visited.add((1, 1))

        end = stones[-1]
        stones = set(stones)
        if 1 not in stones:
            return False

        queue = [(1, 1)]
        while queue:
            s, k = queue.pop()
            for m in [k - 1, k, k + 1]:
                if s + m == end:
                    return True
                elif m > 0 and s + m in stones and (s + m, m) not in visited:
                    visited.add((s + m, m))
                    queue.append((s + m, m))
        return False


if __name__ == '__main__':
    s = Solution()
    s.canCross([0, 1, 2, 3, 4, 8, 9, 11])
    s.canCross([0, 1, 3, 5, 6, 8, 12, 17])
