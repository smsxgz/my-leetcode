class Solution:
    INF = 2**31 - 1

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            y = 0
            while x > 0:
                y = y * 10 + x % 10
                x = x // 10
            if y > self.INF:
                y = 0
            return y
        else:
            return -self.reverse(-x)
