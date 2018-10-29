class Solution(object):
    ADD_DICT = {
        '0': '1',
        '1': '2',
        '2': '3',
        '3': '4',
        '4': '5',
        '5': '6',
        '6': '7',
        '7': '8',
        '8': '9',
    }

    SUB_DICT = {
        '2': '1',
        '1': '0',
        '3': '2',
        '4': '3',
        '5': '4',
        '6': '5',
        '7': '6',
        '8': '7',
        '9': '8'
    }

    def str_add_one(self, s):
        idx = len(s) - 1
        while s[idx] == '9':
            idx -= 1
        return s[:idx] + self.ADD_DICT[s[idx]] + '0' * (len(s) - idx - 1)

    def str_sub_one(self, s):
        idx = len(s) - 1
        while s[idx] == '0':
            idx -= 1
        return s[:idx] + self.SUB_DICT[s[idx]] + '9' * (len(s) - idx - 1)

    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        length = len(n)
        if length == 1:
            return self.SUB_DICT[n]

        elif n == '9' * length:
            return '1' + '0' * (length - 1) + '1'

        elif n == '1' + '0' * (length - 2) + '1' or n == '1' + '0' * (
                length - 1):
            return '9' * (length - 1)

        m = (length + 1) // 2
        prefix = n[:m]

        s1 = prefix + prefix[length - m - 1::-1]
        if s1 == n:
            nprefix = self.str_sub_one(prefix)
            s1 = nprefix + nprefix[length - m - 1::-1]

        num = int(n)
        delta = int(s1) - num
        print(delta)
        if delta > 0:
            nprefix = self.str_sub_one(prefix)
            s2 = nprefix + nprefix[length - m - 1::-1]
            if num - int(s2) <= delta:
                return s2
        else:
            nprefix = self.str_add_one(prefix)
            s2 = nprefix + nprefix[length - m - 1::-1]
            if int(s2) - num < -delta:
                return s2

        return s1


if __name__ == '__main__':
    s = Solution()
    s.nearestPalindromic('11011')
