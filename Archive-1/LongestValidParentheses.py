class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxp_so_far = dict()
        maxp_so_far[0] = 0
        for i, ch in enumerate(s[1:], 1):
            k = maxp_so_far[i - 1]
            if ch == ')' and i - k - 1 >= 0 and s[i - k - 1] == '(':
                maxp_so_far[i] = k + 2
                if i - k - 2 >= 0 and s[i - k - 2] == ')':
                    maxp_so_far[i] += maxp_so_far[i - k - 2]
                # print(i, maxp_so_far[i])
            else:
                maxp_so_far[i] = 0

        return max(maxp_so_far.values())

    def longestValidParentheses1(self, s):
        maxp = 0
        stack = [-1]
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop(-1)
                if not stack:
                    stack.append(i)
                else:
                    maxp = max(maxp, i - stack[-1])

        return maxp


if __name__ == '__main__':
    s = Solution()
    s.longestValidParentheses1("(((((())))")
    s.longestValidParentheses1("(()))())(")
