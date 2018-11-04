class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) <= 2:
            return len(points)
        maxNumOfPoints = 0
        for i in range(len(points)):
            table = {'90': 1}
            samePoint = 0
            for j in range(i + 1, len(points)):
                if (points[i].x == points[j].x and points[i].y == points[j].y):
                    samePoint += 1
                    continue
                if (points[i].x == points[j].x):
                    angle = '90'
                else:
                    temp = gcd(points[i].y - points[j].y,
                               points[i].x - points[j].x)
                    angle = ((points[i].y - points[j].y) // temp,
                             (points[i].x - points[j].x) // temp)
                if angle not in table:
                    table[angle] = 1
                table[angle] += 1
            maxNumOfPoints = max(maxNumOfPoints,
                                 max(table.values()) + samePoint)

        return maxNumOfPoints


if __name__ == '__main__':
    case = [[1, 1], [2, 2], [3, 3]]
    case = [Point(*p) for p in case]
    s = Solution()
    s.maxPoints(case)
