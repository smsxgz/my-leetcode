class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0

        for i in range(len(matrix)):
            for j in range((len(matrix[0]))):
                if matrix[i][j] == '1':
                    if i > 0:
                        matrix[i][j] = matrix[i - 1][j] + 1
                    else:
                        matrix[i][j] = 1
                else:
                    matrix[i][j] = 0

        return max(self.largestRectangleArea(line) for line in matrix)

    def largestRectangleArea(self, heights):
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

        return max(h * (ne - pr) for h, ne, pr in zip(heights, next, prev))

    def maximalRectangle1(self, matrix):
        nums = [int(''.join(row), 2) for row in matrix]
        res = 0
        n = len(nums)
        for start in range(n):
            num = nums[start]
            end = start
            while end < n:
                num &= nums[end]
                if not num:
                    break
                # find now the number of continous `1`
                cnt = 0
                new_num = num
                while new_num:
                    cnt += 1
                    new_num &= (num << cnt)
                res = max(res, (end - start + 1) * cnt)
                end += 1
        return res


if __name__ == '__main__':
    s = Solution()
    s.maximalRectangle([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
                        ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]])
