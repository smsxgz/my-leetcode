class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = -1
        r = len(nums) - 1

        while l < r:
            mid = (l + r + 1) // 2
            if nums[mid] < target:
                l = mid
            else:
                r = mid - 1
        low = l

        l = 0
        r = len(nums)

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid
            else:
                l = mid + 1

        up = l
        if up - low < 2:
            return [-1, -1]
        else:
            return [low + 1, up - 1]


if __name__ == '__main__':
    s = Solution()
    s.searchRange([2], 2)
