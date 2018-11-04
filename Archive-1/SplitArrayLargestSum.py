class Solution:
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        n = len(nums)
        dp = dict((k, [0 for _ in range(n)]) for k in range(1, m + 1))

        temp_sum = 0
        for i in range(n):
            temp_sum += nums[i]
            dp[1][i] = temp_sum

        for k in range(2, m + 1):
            j = k - 2
            temp_sum = 0
            for i in range(k - 1, n):
                temp_sum += nums[i]
                while dp[k - 1][j + 1] < temp_sum - nums[j + 1]:
                    temp_sum -= nums[j + 1]
                    j += 1
                dp[k][i] = min(dp[k - 1][j + 1], max(dp[k - 1][j], temp_sum))

        return dp[m][n - 1]

    def splitArray1(self, nums, m):
        def _solve(target, nums, m):
            temp_sum = 0
            for n in nums:
                if temp_sum + n > target:
                    m -= 1
                    temp_sum = n
                    if n > target:
                        return False
                else:
                    temp_sum += n

            return m >= 1

        L, R = 0, sum(nums) + 1
        while L < R:
            mid = (L + R) // 2
            if _solve(mid, nums, m):
                R = mid
            else:
                L = mid + 1
        return R


if __name__ == '__main__':
    s = Solution()
    s.splitArray1([7, 2, 5, 10, 8], 2)
