class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        nums = {
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '0': 0
        }
        t = 0
        st = 0
        for char in str:
            if char in [' ', '\t'] and st == 0:
                continue
            elif char in ['+', '-']:
                if st != 0:
                    break
                if char == '-':
                    st = -1
                else:
                    st = 1
            elif char in nums:
                t = t * 10 + nums[char]
                if st == 0:
                    st = 1
            else:
                break
        t = t * st
        if t > 2147483647:
            return 2147483647
        elif t < -2147483648:
            return -2147483648
        else:
            return t
