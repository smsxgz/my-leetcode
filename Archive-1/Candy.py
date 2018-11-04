class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candies = 1
        direction = 1
        n = len(ratings)
        last = 1
        for idx in range(1, n):
            if ratings[idx] > ratings[idx - 1]:
                if direction > 0:
                    direction += 1
                else:
                    candies += max(-direction - last, 0)
                    candies += (-direction - 1) * (-direction) // 2
                    direction = 2
            elif ratings[idx] < ratings[idx - 1]:
                if direction < 0:
                    direction -= 1
                else:
                    candies += direction * (direction + 1) // 2 - 1
                    last = direction
                    direction = -2
            else:
                if direction > 0:
                    candies += direction * (direction + 1) // 2 - 1
                    last = direction
                else:
                    candies += max(-direction - last, 0)
                    candies += (-direction - 1) * (-direction) // 2
                candies += 1
                direction = 1

        if direction > 0:
            candies += direction * (direction + 1) // 2 - 1
            last = direction
        else:
            candies += max(-direction - last, 0)
            candies += (-direction - 1) * (-direction) // 2

        return candies


if __name__ == '__main__':
    s = Solution()
    s.candy([1, 2, 2, 1])
