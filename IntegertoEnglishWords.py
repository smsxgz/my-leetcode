class Solution(object):
    one = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine'
    }
    ten = {
        10: 'Ten',
        11: 'Eleven',
        12: 'Twelve',
        13: 'Thirteen',
        14: 'Fourteen',
        15: 'Fifteen',
        16: 'Sixteen',
        17: 'Seventeen',
        18: 'Eighteen',
        19: 'Nineteen',
        2: 'Twenty',
        3: 'Thirty',
        4: 'Forty',
        5: 'Fifty',
        6: 'Sixty',
        7: 'Seventy',
        8: 'Eighty',
        9: 'Ninety'
    }

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'

        conjunction = ['Thousand', 'Million', 'Billion']
        res = self._digits3_to_words(num % 1000)
        num = num // 1000
        idx = 0
        while num > 0:
            tmp = self._digits3_to_words(num % 1000)
            if tmp:
                res = tmp + [conjunction[idx]] + res
            idx += 1
            num = num // 1000

        return ' '.join(res)

    def _digits2_to_words(self, num):
        if num == 0:
            return []
        elif num < 10:
            return [self.one[num]]
        elif num < 20:
            return [self.ten[num]]
        else:
            if num % 10 == 0:
                return [self.ten[num // 10]]
            else:
                return [self.ten[num // 10], self.one[num % 10]]

    def _digits3_to_words(self, num):
        if num == 0:
            return []
        elif num < 100:
            return self._digits2_to_words(num)
        else:
            return [self.one[num // 100], 'Hundred'] + self._digits2_to_words(
                num % 100)


if __name__ == '__main__':
    s = Solution()
    s.numberToWords(1000000)
