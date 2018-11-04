class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        for i in range(n - 1):
            res = self.count_say(res)
        return res

    def count_say(self, string):
        s = ''
        n = 0
        res = ''
        for t in string:
            if t == s:
                n += 1
            else:
                if n > 0:
                    res += str(n) + s
                n = 1
                s = t
        return res + str(n) + s


if __name__ == '__main__':
    s = Solution()
    s.countAndSay(4)
