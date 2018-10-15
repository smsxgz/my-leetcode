def _search(stack, y_list):
    n = len(stack)
    if n == 0:
        return [min(y_list)]
    end = stack[-1]
    add = False
    cache = []
    for y in y_list:
        if y > end:
            if add:
                stack[n] = min(y, stack[n])
            else:
                stack.append(y)
                add = True
            continue

        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if stack[mid] == y:
                left = right = mid
            elif stack[mid] < y:
                left = mid + 1
            else:
                right = mid
        cache.append((left, y))
    for idx, y in cache:
        stack[idx] = min(stack[idx], y)

    return stack


class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        n = len(envelopes)
        if n == 0 or n == 1:
            return n
        envelopes = sorted(envelopes, key=lambda x: x[0])

        stack = []
        tmp_y_list = []
        tmp_x = envelopes[0][0]
        for x, y in envelopes:
            if x > tmp_x:
                stack = _search(stack, tmp_y_list)
                print(stack)
                tmp_y_list = [y]
                tmp_x = x
            else:
                tmp_y_list.append(y)
        stack = _search(stack, tmp_y_list)
        return len(stack)

    def maxEnvelopes1(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        import bisect
        if envelopes is None or len(envelopes) == 0:
            return 0

        envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))  # !!!!!
        height = [j[1] for i, j in enumerate(envelopes)]

        dp = []
        for h in height:
            idx = bisect.bisect_left(dp, h)
            if idx == len(dp):
                dp.append(h)
            else:
                dp[idx] = h
        return len(dp)


if __name__ == '__main__':
    s = Solution()
    s.maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]])
    s.maxEnvelopes([[2, 100], [3, 200], [4, 300], [5, 500], [5, 400], [5, 250],
                    [6, 370], [6, 360], [7, 380]])
    s.maxEnvelopes([[3, 5], [7, 8], [3, 6], [3, 10], [7, 20], [17, 3],
                    [17, 45]])  # 3
