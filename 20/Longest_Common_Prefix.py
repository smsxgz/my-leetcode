class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        s = strs.pop(0)
        r = ''
        flag = True
        for i, a in enumerate(s):
            for t in strs:
                try:
                    if t[i] != a:
                        flag = False
                        break
                except IndexError:
                    flag = False
                    break
            if not flag:
                break

            r += a
        return r
