class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2**31 - 1
        if divisor == 0:
            return MAX_INT

        if dividend == 0:
            return 0

        if dividend > 0 and divisor > 0:
            s = 1
        elif dividend < 0 and divisor < 0:
            s = 1
            dividend, divisor = -dividend, -divisor
        elif dividend < 0 and divisor > 0:
            s = -1
            dividend = -dividend
        else:
            s = -1
            divisor = -divisor

        if divisor == 1:
            i = dividend
        else:
            i = self._divice(dividend, divisor)

        if s == 1:
            if i > MAX_INT:
                return MAX_INT
            return i
        else:
            if -i < -MAX_INT - 1:
                return -MAX_INT - 1
            return -i

    def _divice(self, dividend, divisor):
        power = 1
        while dividend > divisor:
            divisor <<= 1
            power <<= 1

        if divisor == dividend:
            return power
        else:
            divisor >>= 1
            power >>= 1

        div = 0
        res = 0
        while power > 0:
            mid = divisor + div
            if mid <= dividend:
                res += power
                div = mid
            divisor >>= 1
            power >>= 1
        return res


if __name__ == '__main__':
    s = Solution()
    s._divice(1, 5)
