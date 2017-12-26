class Solution(object):
    def combinationSum1(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        return self.search_results(candidates, target)

    def search_results(self, candidates, target):
        c = candidates[0]
        if len(candidates) == 1:
            if target % c == 0:
                return [[c] * (target // c)]
            else:
                return []
        if c > target:
            return []

        result = []
        base = []
        while target > 0:
            for r in self.search_results(candidates[1:], target):
                result.append(base + r)
            target -= c
            base.append(c)
        if target == 0:
            result.append(base)
        return result

    #############################################
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        _path = []
        candidates.sort()  # sort the candidate values
        pos = 0
        self.dfs(candidates, target, pos, _path, res)
        return res

    def dfs(self, candidates, target, pos, _path, res):
        if (target == 0):
            res.append(_path[:])
            return

        while (pos < len(candidates) and candidates[pos] <= target):
            _path.append(candidates[pos])
            self.dfs(candidates, target - candidates[pos], pos, _path, res)
            _path.pop()  # backtrack
            pos += 1


if __name__ == '__main__':
    s = Solution()
    s.combinationSum([2, 3, 6, 7], 7)
