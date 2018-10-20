class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        saved = set()
        size = 0
        for x1, y1, x2, y2 in rectangles:
            for p in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if p not in saved:
                    saved.add(p)
                else:
                    saved.remove(p)
            size += (x2 - x1) * (y2 - y1)

        if len(saved) != 4:
            return False

        corners = sorted(saved, key=lambda x: (x[0], x[1]))

        if (corners[3][0] - corners[1][0]) * (
                corners[3][1] - corners[2][1]) != size:
            return False
        return True
