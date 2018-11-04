class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        pos = 0
        s = 1
        return self.search_results(candidates, target, pos, s)

    def search_results(self, candidates, target, pos, s):
        c = candidates[pos]
        if c > target:
            return []
        if c == target:
            return [[c]]
        if pos == len(candidates) - 1 and c < target:
            return []
        result = []
        if s == 1 or candidates[pos] != candidates[pos - 1]:
            for r in self.search_results(candidates, target - c, pos + 1, 1):
                result.append([c] + r)

        for r in self.search_results(candidates, target, pos + 1, 0):
            result.append(r)

        return result


if __name__ == '__main__':
    s = Solution()
    s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
