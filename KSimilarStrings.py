class Solution(object):
    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if A == B:
            return 0
        if len(A) != len(B):
            return -1

        if sorted(list(A)) != sorted(list(B)):
            return -1

        tmp_A, tmp_B = [], []
        for s, t in zip(A, B):
            if s != t:
                tmp_A.append(s)
                tmp_B.append(t)

        return len(tmp_A) - bfs(tmp_A, tmp_B)


def bfs(A, B):
    n = len(A)
    if n == 0:
        return 0
    elif n == 2 or n == 3:
        return 1

    forward = [B[0]]
    end = A[0]
    saved = {B[0]: [[0]], end: []}
    while forward:
        s = forward.pop(0)
        for i in range(1, n):
            if A[i] == s:
                if B[i] == end:
                    saved[B[i]].extend([path + [i] for path in saved[s]])
                elif B[i] not in saved:
                    saved[B[i]] = [path + [i] for path in saved[s]]
                    forward.append(B[i])

    res = 0
    for path in saved[end]:
        tmp_A = [A[i] for i in range(n) if i not in path]
        tmp_B = [B[i] for i in range(n) if i not in path]
        res = max(res, 1 + bfs(tmp_A, tmp_B))
    return res


if __name__ == '__main__':
    s = Solution()
    A = "aabbccddee"
    B = "cdacbeebad"
    s.kSimilarity(A, B)
