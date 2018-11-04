class Solution(object):
    def sumSubseqWidths1(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        n = len(A)
        res = 0
        p = 1
        for idx in range(n):
            res += p * (A[idx] - A[n - idx - 1])
            res %= 10**9 + 7
            p *= 2
        return res

    # More beautiful code!!!
    def sumSubseqWidths(self, A):
        A.sort()
        res = 0
        for i in range(len(A)):
            res *= 2
            res -= A[i]
            res += A[~i]
            res %= 10**9 + 7
        return res
