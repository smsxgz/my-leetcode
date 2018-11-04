class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n <= 2:
            return 0

        stack = []
        saved = []
        for h in height:
            num = 0
            while stack and h >= stack[-1][0]:
                tmp = stack.pop(-1)
                num += tmp[1]

                if len(stack) == 0:
                    saved.append((min(tmp[0], h), num))
                    num = 0

            stack.append((h, num + 1))

        saved.extend(stack)
        return sum(t[0] * t[1] for t in saved) - sum(height)

    # more clever solution
    def trap1(self, height):
        res = 0
        top = 0
        for i in range(len(height)):
            if height[top] < height[i]:
                top = i
        second_top = 0
        for i in range(top):
            if height[second_top] < height[i]:
                second_top = i
            res += height[second_top] - height[i]

        second_top = len(height) - 1
        for i in reversed(range(top, len(height))):
            if height[second_top] < height[i]:
                second_top = i
            res += height[second_top] - height[i]
        return res


if __name__ == '__main__':
    s = Solution()
    s.trap([5, 2, 1, 2, 1, 5])
    s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
