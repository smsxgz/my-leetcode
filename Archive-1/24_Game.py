class frac(object):
    def __init__(self, p, q=1):
        self.p = p
        self.q = q

    def __str__(self):
        return '{}/{}'.format(self.p, self.q)


def mul(x, y):
    return frac(x.p * y.p, x.q * y.q)


def div(x, y):
    if y.p != 0:
        return frac(x.p * y.q, x.q * y.p)


def add(x, y):
    return frac(x.p * y.q + x.q * y.p, x.q * y.q)


def sub(x, y):
    return frac(x.p * y.q - x.q * y.p, x.q * y.q)


def generator(x, y):
    yield mul(x, y)
    yield add(x, y)
    yield sub(x, y)
    yield sub(y, x)
    z = div(x, y)
    if z:
        yield z
    z = div(y, x)
    if z:
        yield z


class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if self._judge([frac(n) for n in nums]):
            return True
        else:
            return False

    def _judge(self, nums):
        l = len(nums)
        if l == 2:
            x, y = nums
            for z in generator(x, y):
                if z.p == 24 * z.q:
                    return True
        else:
            for i in range(l - 1):
                for j in range(i + 1, l):
                    x, y = nums[i], nums[j]
                    e = list(range(l))
                    e.remove(i)
                    e.remove(j)
                    e = [nums[k] for k in e]
                    for z in generator(x, y):
                        if self._judge([z] + e):
                            return True


if __name__ == '__main__':
    s = Solution()
    s.judgePoint24([11, 11, 11, 11])
