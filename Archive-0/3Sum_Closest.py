class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        Min, Max = sum(nums[:3]), sum(nums[-3:])
        if Min >= target:
            return Min
        if Max <= target:
            return Max
        if target - Min < Max - target:
            res = Min
            diff = target - Min
        else:
            res = Max
            diff = Max - target

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                dis = abs(target - s)
                if dis < diff:
                    res = s
                    diff = dis
                if s == target:
                    return res
                elif s < target:
                    if nums[i] + nums[r] * 2 < target:
                        break
                    l += 1
                else:
                    if nums[i] + nums[l] * 2 > target:
                        break
                    r -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    s.threeSumClosest([1, 2, 5, 10, 11], 12)
