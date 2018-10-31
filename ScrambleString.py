class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        cache = dict()

        def _solve(s1, s2):
            if (s1, s2) in cache:
                return cache[(s1, s2)]

            if len(s1) != len(s2):
                cache[(s1, s2)] = False
                return False

            if len(s1) == 1:
                res = s1 == s2
                cache[(s1, s2)] = res
                return res

            count = [0] * 26
            for ch1, ch2 in zip(s1, s2):
                count[ord(ch1) - ord('a')] += 1
                count[ord(ch2) - ord('a')] -= 1

            if any(count):
                cache[(s1, s2)] = False
                return False

            res = False
            n = len(s1)
            for i in range(1, len(s1)):
                if self.isScramble(s1[:i], s2[:i]) and self.isScramble(
                        s1[i:], s2[i:]):
                    res = True
                    break
                elif self.isScramble(s1[:i], s2[n - i:]) and self.isScramble(
                        s1[i:], s2[:n - i]):
                    res = True
                    break

            cache[(s1, s2)] = res
            return res

        return _solve(s1, s2)


if __name__ == '__main__':
    s = Solution()
    s.isScramble("abcde", "caebd")
