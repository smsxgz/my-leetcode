class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        m = {'(': ')', '[': ']', '{': '}'}

        q = []
        for char in s:
            if char in ["(", "{", "["]:
                q.append(char)
            elif char in [")", "}", "]"]:
                if len(q) > 0 and char == m[q[-1]]:
                    q.pop()
                else:
                    return False
        if len(q) > 0:
            return False
        else:
            return True
