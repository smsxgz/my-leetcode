class Solution(object):
    DICT = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []
        if len(digits) == 1:
            return list(self.DICT[digits[0]])

        char = digits[0]
        out = []
        for l in self.letterCombinations(digits[1:]):
            for c in self.DICT[char]:
                out.append(c + l)
        return out
