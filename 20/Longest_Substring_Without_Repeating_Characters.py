class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        t = ''
        tmax = 0
        for char in s:
            if char in t:
                i = t.index(char)
                t = t[i + 1:] + char
            else:
                t += char
                lt = len(t)
                if lt > tmax:
                    tmax = lt
            print(t)
        return tmax


if __name__ == "__main__":
    s = Solution()
    s.lengthOfLongestSubstring('bpfbhmipx')
