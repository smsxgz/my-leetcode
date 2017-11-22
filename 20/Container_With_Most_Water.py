class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        S = (right - left) * min(height[left], height[right])

        while left < right:
            x, y = height[left], height[right]
            if x > y:
                S = max(S, (right - left) * y)
                right -= 1
            else:
                S = max(S, (right - left) * x)
                left += 1
        return S
