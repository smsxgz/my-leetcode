class Solution:
    def findMin(self, nums):
        """
        no duplicate
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while right > left:
            if nums[right] > nums[left]:
                return nums[left]

            else:
                mid = (right + left) // 2
                if nums[mid] >= nums[left]:
                    left = mid + 1
                else:
                    right = mid

        return nums[left]

    def findMin1(self, nums):
        """
        may have duplicates
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while right > left:
            if nums[right] > nums[left]:
                return nums[left]

            elif nums[right] == nums[left]:
                right -= 1
                left += 1

            else:
                mid = (right + left) // 2
                if nums[mid] >= nums[left]:
                    left = mid + 1
                elif nums[mid] < nums[left]:
                    right = mid

        return nums[left]


if __name__ == '__main__':
    s = Solution()
    s.findMin([4, 5, 6, 7, 0, 1, 2])
    s.findMin1([10, 10, 10, 10, 10])
