class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n in [0, 1]:
            return n

        i = 0
        for j in range(1, n):
            if nums[j] > nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1


if __name__ == '__main__':
    s = Solution()
    l = [1, 2, 2, 3, 3, 4, 5, 6, 6, 6, 6]
    s.removeDuplicates(l)
    l
