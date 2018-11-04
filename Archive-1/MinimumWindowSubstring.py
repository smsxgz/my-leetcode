from collections import Counter


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        tc = Counter(t)
        n = len(s)
        m = len(t)

        tmp = Counter(s)
        if any(tmp[c] < tc[c] for c in tc):
            return ""

        i = 0
        while True:
            if s[i] in tc:
                break
            i += 1
        j = i

        minw = s[i:]
        counter = Counter()
        while i <= n - m and j <= n:
            # print(i, j, s[i:j])
            if s[i] not in tc:
                i += 1
                continue

            for c in tc:
                if counter[c] < tc[c]:
                    break

            else:
                if j - i < len(minw):
                    minw = s[i:j]
                counter[s[i]] -= 1
                i += 1
                continue

            if j == n:
                break
            ch = s[j]
            j += 1
            counter[ch] += 1

        return minw

    def minWindow1(self, s, t):
        if not s or not t or len(s) < len(t):
            return ""

        T = Counter(t)

        missing = len(t)
        i = l = r = 0
        for j, c in enumerate(s, 1):
            if T[c] > 0:
                missing -= 1
            T[c] -= 1

            if not missing:
                while i < j and T[s[i]] < 0:
                    T[s[i]] += 1
                    i += 1
                if not r or j - i < r - l:
                    l, r = i, j
                T[s[i]] += 1
                i += 1
                missing += 1

        return s[l:r]


if __name__ == '__main__':
    s = Solution()
    # s.minWindow("ADOBECODEBANC", "ABC")
    s.minWindow("cabwefgewcwaefgcf", "cae")
