"""
https://leetcode.com/problems/rectangle-area-ii/
"""

"""
https://leetcode.com/problems/rectangle-area-ii/
"""


class Solution:
    def rectangleArea(self, rectangles: list[list[int]]) -> int:
        """
        1. Suppose there is an infinite horizontal line moving from the bottom
            to the top of each rectangle.
        2. For each rectangle:
            2.1 when the line reaching its bottom, it will add
                a span (x1, x2) to the line.
            2.2 When the line reaching its top, it will remove a span
                (x1, x2) from the line.
        3. Then we could record those add or remove events and sort them
            in asending order, then start to calculate the area when the line
            is moving from one y to another y.
        4. Between each y, the span of x is calculated by checking if any
            range from adjancent two elements have a non-zero counter.
        """
        xs = sorted(set(x for x1, _, x2, _ in rectangles for x in [x1, x2]))
        xi = {x: i for i, x in enumerate(xs)}
        N = len(xs)
        count = [0] * N
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, x1, x2, 1))  # open
            events.append((y2, x1, x2, -1))  # close

        events.sort()
        currY = currXSum = area = 0  # All the rectangles are above x axis.
        for y, x1, x2, offset in events:
            area += (y - currY) * currXSum
            currY = y
            for i in range(xi[x1], xi[x2]):
                count[i] += offset

            currXSum = sum(
                x2 - x1 for x1, x2, cnt in zip(xs, xs[1:], count) if cnt)

        return area % (10 ** 9 + 7)
