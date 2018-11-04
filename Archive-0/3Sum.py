class Solution(object):
    def twoSum(self, nums, target, i0):
        if len(nums) > 1:
            buff_dict = set()
            for n in nums:
                if n in buff_dict:
                    yield [target - n, n]
                else:
                    buff_dict.add(target - n)

    def threeSum1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        for i, n in enumerate(nums):
            for lt in self.twoSum(nums[i + 1:], -n, i + 1):
                out = self.threesort([n] + lt)
                if out not in output:
                    output.append(out)
        return output

    def threesort(self, nums):
        a, b, c = nums
        if a > b:
            a, b = b, a
        if b > c:
            b, c = c, b
        if a > b:
            a, b = b, a
        return [a, b, c]

    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res


if __name__ == "__main__":
    l = [-1, 0, 1, 2, -1, -4]
    s = Solution()
    s.threeSum(l)
