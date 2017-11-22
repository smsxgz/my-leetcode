class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        y = 0
        z = x
        while z > 0:
            y = y * 10 + (z % 10)
            z = z // 10
        return (x == y)


if __name__ == '__main__':
    s = Solution()
    s.isPalindrome(1)
