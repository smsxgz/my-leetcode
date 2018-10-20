class Bucket:
    def __init__(self, val):
        self.minval = val
        self.maxval = val


class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0

        a = max(nums)
        b = min(nums)
        if a == b:
            return 0
        d = max(1, (a - b) // (len(nums) - 1))

        record = {}
        for n in nums:
            i = (n - b) // d
            if i in record:
                obj = record[i]
                obj.minval = min(obj.minval, n)
                obj.maxval = max(obj.maxval, n)
            else:
                record[i] = Bucket(n)

        maxgap = d
        prev_maxval = b
        for i in range(len(nums)):
            try:
                obj = record[i]
            except Exception:
                continue
            maxgap = max(obj.minval - prev_maxval, maxgap)
            prev_maxval = obj.maxval

        return maxgap


if __name__ == '__main__':
    s = Solution()
    s.maximumGap([3, 6, 9, 1])
