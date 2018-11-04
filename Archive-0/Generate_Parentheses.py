class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = {}
        res[0] = [""]

        for m in range(1, n + 1):
            res[m] = ['(' + s + ')' for s in res[m - 1]]
            for i in range(1, m):
                res[m].extend([
                    t + '(' + s + ')' for t in res[i] for s in res[m - 1 - i]
                ])
            print(res[m])
        return res[n]

    def generateParenthesis1(self, n):
        res = []
        path = ''
        left = n
        right = n
        self.dfs(left, right, path, res)
        return res

    def dfs(self, left, right, path, res):
        if left < right:
            return
        if not left and not right:
            res.append(path)
            return
        if left:
            self.dfs(left - 1, right, path + ')', res)
        if right:
            self.dfs(left, right - 1, path + '(', res)


if __name__ == '__main__':
    s = Solution()
    s.generateParenthesis(3)
