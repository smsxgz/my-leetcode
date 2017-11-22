class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = '\0' + '\0'.join(list(s)) + '\0'
        l = len(s)
        ix = 0
        mx = 0
        p = []

        out = ''
        outl = 0
        for i in range(l):
            if mx > i:
                tmp = min(p[2 * ix - i], mx - i)
            else:
                tmp = 1
            while i + tmp < l and i - tmp >= 0 and s[i + tmp] == s[i - tmp]:
                tmp += 1
            p.append(tmp)
            if tmp - 1 > outl:
                outl = tmp - 1
                out = s[i - tmp + 1:i + tmp]
            if i + tmp > mx:
                mx = i + tmp
                ix = i
        if out[0] == '\0':
            return out[1::2]
        return out[::2]


if __name__ == "__main__":
    s = Solution()
    s.longestPalindrome('aa')
