"""
https://leetcode.com/problems/boats-to-save-people/
"""


from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        weights = sorted(people)
        l, r, boats = 0, len(weights) - 1, 0
        while l <= r:
            # Either the heaviest person cannot be paird with any other people
            # or it could pair with the lightest person. Both case will take
            # 1 boat.
            boats += 1

            # When the lightest person takes the boat, advance the pointer to
            # the next lightest person.
            if weights[l] + weights[r] <= limit:
                l += 1

            r -= 1  # Point to the next heaviest person.

        return boats


print(Solution().numRescueBoats([3, 5, 3, 4], 5))
