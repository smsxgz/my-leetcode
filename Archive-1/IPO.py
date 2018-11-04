import heapq


class Solution:
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        assert len(Capital) == len(Profits)
        pc = list(zip(Profits, Capital))
        pc.sort(reverse=True)

        for _ in range(k):
            for i in range(len(pc)):
                if pc[i][1] <= W:
                    W += pc[i][0]
                    pc.pop(i)
                    break
            else:
                break

        return W

    def findMaximizedCapital1(self, k, W, Profits, Capital):
        available_heap = []
        unavailable_heap = []
        for p, c in zip(Profits, Capital):
            if c > W:
                unavailable_heap.append((c, p))
            else:
                available_heap.append(-p)
        if not available_heap:
            return 0

        heapq.heapify(available_heap)
        heapq.heapify(unavailable_heap)

        for _ in range(k):
            while unavailable_heap and unavailable_heap[0][0] <= W:
                (_, p) = heapq.heappop(unavailable_heap)
                heapq.heappush(available_heap, -p)
            if available_heap:
                W += -heapq.heappop(available_heap)
            else:
                break
        return W


if __name__ == '__main__':
    s = Solution()
    s.findMaximizedCapital(50000, 50000, list(range(50000)), list(
        range(50000)))
