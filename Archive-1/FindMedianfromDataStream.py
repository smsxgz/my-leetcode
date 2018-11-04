import heapq


class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if len(self.nums) == 0 or num >= self.nums[-1]:
            self.nums.append(num)
        else:
            l, r = 0, len(self.nums) - 1
            while r > l:
                mid = (l + r) // 2
                if self.nums[mid] < num:
                    l = mid + 1
                else:
                    r = mid
            self.nums.insert(l, num)
        print(self.nums)

    def findMedian(self):
        """
        :rtype: float
        """
        n = len(self.nums)
        if n % 2 == 0:
            return (self.nums[n // 2 - 1] + self.nums[n // 2]) / 2.0
        else:
            return self.nums[n // 2] * 1.0


class MedianFinder1(object):
    def __init__(self):
        self.left_heap = []
        self.right_heap = []
        self.balance = 0

    def __repr__(self):
        return 'left: {}\nright: {}\nbalance: {}'.format(
            self.left_heap, self.right_heap, self.balance)

    def addNum(self, num):
        if len(self.left_heap) == 0:
            self.left_heap.append(-num)
            self.balance = 1

        elif self.balance == 0:
            if num > -self.left_heap[0]:
                heapq.heappush(self.right_heap, num)
                self.balance = -1
            else:
                heapq.heappush(self.left_heap, -num)
                self.balance = 1

        elif self.balance == 1:
            if num >= -self.left_heap[0]:
                heapq.heappush(self.right_heap, num)
            else:
                temp = -heapq.heappop(self.left_heap)
                heapq.heappush(self.left_heap, -num)
                heapq.heappush(self.right_heap, temp)
            self.balance = 0

        else:
            if num <= self.right_heap[0]:
                heapq.heappush(self.left_heap, -num)
            else:
                temp = heapq.heappop(self.right_heap)
                heapq.heappush(self.right_heap, num)
                heapq.heappush(self.left_heap, -temp)
            self.balance = 0

        print(self)

    def findMedian(self):
        if self.balance == 1:
            return -self.left_heap[0] * 1.0
        elif self.balance == -1:
            return self.right_heap[0] * 1.0
        else:
            return (-self.left_heap[0] + self.right_heap[0]) / 2.0


if __name__ == '__main__':
    s = MedianFinder1()
    s.addNum(12)
    s.addNum(10)
    s.addNum(13)
    s.addNum(11)
    s.addNum(5)

    s.left_heap
    s.right_heap
    s.findMedian()
