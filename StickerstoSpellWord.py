from collections import Counter


class Solution:
    def minStickers(self, stickers, target):
        t_count = Counter(target)
        A = [Counter(sticker) & t_count for sticker in stickers]

        for i in range(len(A) - 1, -1, -1):
            if any(A[i] == A[i] & A[j] for j in range(len(A)) if i != j):
                A.pop(i)

        self.best = len(target) + 1

        def dfs(ans=0):
            if ans >= self.best:
                return
            if not A:
                if all(t_count[letter] <= 0 for letter in t_count):
                    self.best = ans
                return

            sticker = A.pop()
            used = max((t_count[letter] - 1) // sticker[letter] + 1
                       for letter in sticker)
            used = max(used, 0)

            for c in sticker:
                t_count[c] -= used * sticker[c]

            dfs(ans + used)
            for i in range(used - 1, -1, -1):
                for letter in sticker:
                    t_count[letter] += sticker[letter]
                dfs(ans + i)

            A.append(sticker)

        dfs()
        return self.best if self.best <= len(target) else -1


if __name__ == '__main__':
    s = Solution()
    s.minStickers(["notice", "possible"], "basicbasic")
    s.minStickers(["with", "example", "science"], "thehat")
    s.minStickers([
        "control", "heart", "interest", "stream", "sentence", "soil", "wonder",
        "them", "month", "slip", "table", "miss", "boat", "speak", "figure",
        "no", "perhaps", "twenty", "throw", "rich", "capital", "save",
        "method", "store", "meant", "life", "oil", "string", "song", "food",
        "am", "who", "fat", "if", "put", "path", "come", "grow", "box",
        "great", "word", "object", "stead", "common", "fresh", "the",
        "operate", "where", "road", "mean"
    ], "stoodcrease")
