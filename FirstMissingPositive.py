class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for idx, n in enumerate(nums):
            while idx + 1 > n and n > 0:
                m = nums[n - 1]
                if m == n:
                    n = -1
                    break
                nums[n - 1] = n
                n = m
            nums[idx] = n

        for idx, n in enumerate(nums):
            if idx + 1 < n or n <= 0:
                return idx + 1

        return len(nums) + 1


if __name__ == '__main__':
    s = Solution()
    s.firstMissingPositive([1, 1])
