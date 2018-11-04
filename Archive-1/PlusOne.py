class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = []
        tmp = 1
        for d in digits[::-1]:
            res.append((d + tmp) % 10)
            if d + tmp < 10:
                tmp = 0
        if tmp == 1:
            res.append(1)
        return res[::-1]
