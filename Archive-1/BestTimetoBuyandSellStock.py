from heapq import heappush, heappop


class Solution(object):
    def maxProfit1(self, prices):
        """
        only one transaction
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        current_min = prices[0]
        max_profit = 0
        for p in prices[1:]:
            max_profit = max(p - current_min, max_profit)
            current_min = min(p, current_min)

        return max_profit

    def maxProfit2(self, prices):
        """
        as many transactions as you like
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0 or n == 1:
            return 0

        max_profit = 0
        for i in range(n - 2, -1, -1):
            max_profit = max(prices[i + 1] - prices[i], 0) + max_profit

        return max_profit

    def maxProfit3(self, prices, k=2):
        """
        at most k transactions
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0 or n == 1:
            return 0

        pre_max_profit = [0 for _ in range(n)]
        max_profit = [0 for _ in range(n)]
        for kk in range(1, k + 1):
            temp = 0
            for i in range(n - 2, -1, -1):
                temp = max(prices[i + 1] - prices[i] + temp,
                           pre_max_profit[i + 1])
                max_profit[i] = max(temp, max_profit[i + 1])
            pre_max_profit = max_profit.copy()

        return max_profit[0]

    def maxProfit4(self, k, prices):
        length = len(prices)
        if len(prices) < 2 or k < 1:
            return 0

        if k >= len(prices) // 2:
            return sum(prices[i] - prices[i - 1] for i in range(1, length)
                       if prices[i] - prices[i - 1] > 0)
        profit = []
        pairs = []
        j = 0
        while j < length:
            i = j
            while i < length - 1 and prices[i] >= prices[i + 1]:
                i += 1
            j = i + 1
            while j < length and prices[j] >= prices[j - 1]:
                j += 1

            while pairs and prices[i] < prices[pairs[-1][0]]:
                lo, hi = pairs.pop()
                heappush(profit, prices[lo] - prices[hi])
            while pairs and prices[j - 1] >= prices[pairs[-1][1]]:
                lo, hi = pairs.pop()
                heappush(profit, prices[i] - prices[hi])
                i = lo

            pairs.append([i, j - 1])

        while pairs:
            lo, hi = pairs.pop()
            heappush(profit, prices[lo] - prices[hi])

        ans = 0
        while k > 0 and profit:
            ans += -heappop(profit)
            k -= 1

        return ans


if __name__ == '__main__':
    s = Solution()
    s.maxProfit3([3, 3, 5, 0, 0, 3, 1, 4])
