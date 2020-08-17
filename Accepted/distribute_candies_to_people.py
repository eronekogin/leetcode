"""
https://leetcode.com/problems/distribute-candies-to-people/
"""


from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        # First find how many rounds it needs to repeat.
        r, n = 1, num_people
        s, increment = n * (n + 1) // 2, n * n
        while (s + s + (r - 1) * increment) * r // 2 <= candies:
            r += 1

        # Then determine which person is the last one to receive the candy.
        remainCandies = candies - max(
            0, (s + s + (r - 2) * increment) * (r - 1) // 2)
        s, c = 1 + (r - 1) * n, 1
        while (s + s + c - 1) * c // 2 <= remainCandies:
            c += 1

        finalRemainCandies = remainCandies - max(
            0, (s + s + c - 2) * (c - 1) // 2)
        rslt = [0] * n
        for i in range(n):
            if i + 1 < c:
                rslt[i] = (i + 1 + i + 1 + (r - 1) * n) * r // 2
            elif i + 1 == c:
                rslt[i] = max(0, (i + 1 + i + 1 + (r - 2) * n) * (r - 1) // 2)\
                    + finalRemainCandies
            else:
                rslt[i] = max(0, (i + 1 + i + 1 + (r - 2) * n) * (r - 1) // 2)

        return rslt


print(Solution().distributeCandies(7, 4))
