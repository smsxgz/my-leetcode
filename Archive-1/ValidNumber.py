class Solution(object):
    def isNumber(self, strings):
        """
        :type strings: str
        :rtype: bool
        """
        numbers = set('0123456789')
        scientific = False
        decimal = False
        start = False
        end = False
        have_numbers = False

        for i, s in enumerate(strings):
            if s == ' ':
                if start:
                    end = True

            elif s in ['+', '-']:
                if start:
                    return False
                else:
                    start = True
            else:
                if not start:
                    start = True
                elif end:
                    return False

                if s == 'e':
                    if scientific or not have_numbers:
                        return False
                    else:
                        start = False
                        have_numbers = False
                        scientific = True

                elif s == '.':
                    if decimal or scientific:
                        return False
                    else:
                        decimal = True

                elif s in numbers:
                    have_numbers = True

                else:
                    return False

        return have_numbers

    def isNumber2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        nums = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

        hasE = hasFirst = hasDot = hasDigit = False

        for c in s:
            if c in nums:
                hasDigit = hasFirst = True
            elif c == '+' or c == '-':
                if hasFirst:
                    return False
                hasFirst = True
            elif c == 'e':
                if not hasFirst or not hasDigit or hasE:
                    return False
                hasE = hasDot = True
                hasDigit = hasFirst = False
            elif c == '.':
                if hasE or hasDot:
                    return False
                hasDot = hasFirst = True
            else:
                return False
        return hasFirst and hasDigit


if __name__ == '__main__':
    s = Solution()
    s.isNumber2('-1.')
