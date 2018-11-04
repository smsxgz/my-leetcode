class Solution:
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        cache = dict()

        def _solve(i, j, k):
            ch = boxes[i]
            while i < j - 1 and boxes[i + 1] == ch:
                i += 1
                k += 1

            if j - i == 1:
                return (k + 1)**2

            if (i, j, k) in cache:
                return cache[(i, j, k)]

            temp = (k + 1)**2 + _solve(i + 1, j, 0)
            for ii in range(i + 2, j):
                if boxes[ii] == ch:
                    temp = max(temp,
                               _solve(i + 1, ii, 0) + _solve(ii, j, k + 1))

            cache[(i, j, k)] = temp
            return temp

        return _solve(0, len(boxes), 0)


if __name__ == '__main__':
    s = Solution()
    s.removeBoxes([1, 3, 2, 2, 2, 3, 4, 3, 1])
