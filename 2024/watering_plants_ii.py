"""
https://leetcode.com/problems/watering-plants-ii/description
"""


class Solution:
    """
    Solution
    """

    def minimum_refill(self, plants: list[int], capacity_a: int, capacity_b: int) -> int:
        """
        minimum_refill
        """
        a, b = 0, len(plants) - 1
        refills = 0
        wa, wb = capacity_a, capacity_b
        while a <= b:
            if a < b:
                if wa < plants[a]:
                    refills += 1
                    wa = capacity_a - plants[a]
                else:
                    wa -= plants[a]

                if wb < plants[b]:
                    refills += 1
                    wb = capacity_b - plants[b]
                else:
                    wb -= plants[b]

                a += 1
                b -= 1
            else:
                if wa >= wb:
                    if wa < plants[a]:
                        refills += 1
                        wa = capacity_a - plants[a]
                    else:
                        wa -= plants[a]

                    a += 1
                else:
                    if wb < plants[b]:
                        refills += 1
                        wb = capacity_b - plants[b]
                    else:
                        wb -= plants[b]

                    b -= 1

        return refills
