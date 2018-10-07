class Solution(object):
    def makeLargestSpecial(self, S):
        """
        :type S: str
        :rtype: str
        """
        if len(S) == 2:
            return S

        blocks = []
        delta = 0
        left = 0
        for idx, s in enumerate(S):
            if s == '1':
                delta += 1
            else:
                delta -= 1
            if delta == 0:
                tmp = self.makeLargestSpecial(S[left + 1:idx])
                blocks.append('1' + tmp + '0')
                left = idx + 1

        blocks.sort(reverse=True)
        return ''.join(blocks)


if __name__ == '__main__':
    s = Solution()
    s.makeLargestSpecial("11011000")
