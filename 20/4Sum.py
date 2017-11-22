class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums) - 3):
            if sum(nums[i:i + 4]) > target:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + sum(nums[-3:]) < target:
                continue
            for j in range(i + 1, len(nums) - 2):
                if nums[i] + sum(nums[j:j + 3]) > target:
                    break
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + sum(nums[-2:]) < target:
                    continue
                l, r = j + 1, len(nums) - 1
                tmp = nums[i] + nums[j] - target
                while l < r:
                    s = tmp + nums[l] + nums[r]
                    if s < 0:
                        l += 1
                    elif s > 0:
                        r -= 1
                    else:
                        res.append((nums[i], nums[j], nums[l], nums[r]))
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
        return res
