def _roman(m, s1, s2, s3):
    if m <= 3:
        return s1 * m
    elif m <= 4:
        return s1 + s2
    elif m <= 8:
        return s2 + s1 * (m - 5)
    else:
        return s1 + s3


class Solution(object):
    DICT = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        a = num // 1000
        out = 'M' * a
        print(out)

        for n in [100, 10, 1]:
            a = num // n % 10
            out += _roman(a, self.DICT[n], self.DICT[5 * n], self.DICT[10 * n])
            print(out)
        return out


if __name__ == '__main__':
    s = Solution()
    s.intToRoman(1)
