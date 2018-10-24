class Solution:
    def maxSumOfThreeSubarrays1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)

        dp1 = dict()
        temp_sum = sum(nums[:k])
        dp1[k - 1] = {'sum': temp_sum, 'index': 0}
        for i in range(k, n):
            temp_sum += nums[i] - nums[i - k]
            if temp_sum > dp1[i - 1]['sum']:
                dp1[i] = {'sum': temp_sum, 'index': i - k + 1}
            else:
                dp1[i] = dp1[i - 1]

        dp2 = dict()
        temp_sum = sum(nums[k:2 * k])
        dp2[2 * k - 1] = {'sum': dp1[k - 1]['sum'] + temp_sum, 'index': [0, k]}
        for i in range(2 * k, n):
            temp_sum += nums[i] - nums[i - k]
            if dp1[i - k]['sum'] + temp_sum > dp2[i - 1]['sum']:
                dp2[i] = {
                    'sum': dp1[i - k]['sum'] + temp_sum,
                    'index': [dp1[i - k]['index'], i - k + 1]
                }
            else:
                dp2[i] = dp2[i - 1]

        dp3 = dict()
        temp_sum = sum(nums[2 * k:3 * k])
        dp3[3 * k - 1] = {
            'sum': dp2[2 * k - 1]['sum'] + temp_sum,
            'index': [0, k, 2 * k]
        }
        for i in range(3 * k, n):
            temp_sum += nums[i] - nums[i - k]
            if dp2[i - k]['sum'] + temp_sum > dp3[i - 1]['sum']:
                dp3[i] = {
                    'sum': dp2[i - k]['sum'] + temp_sum,
                    'index': dp2[i - k]['index'] + [i - k + 1]
                }
            else:
                dp3[i] = dp3[i - 1]

        return dp3[n - 1]['index']

    def maxSumOfThreeSubarrays(self, nums, k):
        n = len(nums)

        temp_sum = sum(nums[:k])
        sum_memo = {k - 1: temp_sum}
        for i in range(k, n):
            temp_sum += nums[i] - nums[i - k]
            sum_memo[i] = temp_sum

        pre_dp_sum = dict((i, 0) for i in range(n))
        pre_dp_index = dict((i, []) for i in range(n))
        for m in range(1, 4):
            dp_sum = dict()
            dp_index = dict()
            dp_sum[m * k - 1] = pre_dp_sum.get(
                (m - 1) * k - 1, 0) + sum_memo[m * k - 1]
            dp_index[m * k - 1] = [mm * k for mm in range(m)]
            for i in range(m * k, n):
                if pre_dp_sum[i - k] + sum_memo[i] > dp_sum[i - 1]:
                    dp_sum[i] = pre_dp_sum[i - k] + sum_memo[i]
                    dp_index[i] = pre_dp_index[i - k] + [i - k + 1]
                else:
                    dp_sum[i] = dp_sum[i - 1]
                    dp_index[i] = dp_index[i - 1]

            pre_dp_sum = dp_sum
            pre_dp_index = dp_index

        return dp_index[n - 1]

    def maxSumOfThreeSubarrays2(self, nums, k):
        if not nums or not k or k < 0 or len(nums) < 3 * k:
            return [-1] * 3

        n = len(nums)
        c = n - k
        b = n - 2 * k
        a = n - 3 * k

        sumc = sum(nums[c:c + k])
        sumb = sum(nums[b:b + k])
        suma = sum(nums[a:a + k])

        maxc = sumc
        maxb = sumb + maxc
        maxa = suma + maxb

        partc = [c]
        partbc = [b, c]
        ans = [a, b, c]

        while a > 0:
            a -= 1
            b -= 1
            c -= 1

            sumc += nums[c] - nums[c + k]
            sumb += nums[b] - nums[b + k]
            suma += nums[a] - nums[a + k]

            if sumc >= maxc:
                maxc = sumc
                partc = [c]

            if sumb + maxc >= maxb:
                maxb = sumb + maxc
                partbc = [b] + partc

            if suma + maxb >= maxa:
                maxa = suma + maxb
                ans = [a] + partbc

        return ans


if __name__ == '__main__':
    s = Solution()
    s.maxSumOfThreeSubarrays([1, 2, 1, 2, 6, 7, 5, 1], 2)
