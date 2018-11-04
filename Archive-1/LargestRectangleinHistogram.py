class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        if n == 0:
            return 0
        elif n == 1:
            return heights[0]

        stack = []
        next = [n] * n
        prev = [0] * n
        for idx, h in enumerate(heights):
            j = idx
            while stack and h < stack[-1][1]:
                i, s, j = stack.pop(-1)
                next[i] = idx
            prev[idx] = j
            stack.append((idx, h, j))
        print(next, prev)

        return max(h * (ne - pr) for h, ne, pr in zip(heights, next, prev))


if __name__ == '__main__':
    s = Solution()
    s.largestRectangleArea([3, 6, 5, 7, 4, 8, 1, 0])
