class Solution(object):
    DICT = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        out = 0
        i = 0
        l = len(s)
        while i < l - 1:
            char = s[i]
            if char == 'I':
                if s[i + 1] in ['V', 'X']:
                    out += self.DICT[s[i + 1]] - 1
                    i += 2
                else:
                    out += 1
                    i += 1
            elif char == 'X':
                if s[i + 1] in ['L', 'C']:
                    out += self.DICT[s[i + 1]] - 10
                    i += 2
                else:
                    out += 10
                    i += 1
            elif char == 'C':
                if s[i + 1] in ['D', 'M']:
                    out += self.DICT[s[i + 1]] - 100
                    i += 2
                else:
                    out += 100
                    i += 1
            else:
                out += self.DICT[char]
                i += 1
        if i < l:
            out += self.DICT[s[l - 1]]
        return out
