"""
https://leetcode.com/problems/swap-adjacent-in-lr-string/
"""


class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        """
        1. Take L and R as people and X as spaces separate each person.
        2. XL -> LX means an L person could only move to the left.
        3. RX -> XR means a R person could only move to the right.
        4. So in order to transform from start to end, all the Ls in the end
            should on the same or left side of the Ls in the start. All the Rs
            in the end should on the same side or right side of the Rs in
            the start.
        """
        l1, r1, l2, r2, f1, f2 = [], [], [], [], [], []
        for i, c in enumerate(start):
            if c != 'X':
                f1.append(c)
                if c == 'L':
                    l1.append(i)
                else:
                    r1.append(i)

        for i, c in enumerate(end):
            if c != 'X':
                f2.append(c)
                if c == 'L':
                    l2.append(i)
                else:
                    r2.append(i)

        return f1 == f2 and all(s1 >= t1 for s1, t1 in zip(l1, l2)) and \
            all(s2 <= t2 for s2, t2 in zip(r1, r2))


print(Solution().canTransform("RXXLRXRXL", "XRLXXRRLX"))
