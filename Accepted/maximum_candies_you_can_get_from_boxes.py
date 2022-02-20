"""
https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/
"""


class Solution:
    def maxCandies(
        self,
        status: list[int],
        candies: list[int],
        keys: list[list[int]],
        containedBoxes: list[list[int]],
        initialBoxes: list[int]
    ) -> int:
        collectedKeys = set()
        currBoxes = initialBoxes
        candyCnt = 0
        visited = set()
        for box in currBoxes:
            if not status[box]:  # Box is locked.
                if box in collectedKeys:  # Could open the box.
                    candyCnt += candies[box]
                    currBoxes.extend(containedBoxes[box])
                    collectedKeys |= set(keys[box])
                else:  # Have not found the key yet.
                    if box in visited:  # Found loop.
                        break

                    currBoxes.append(box)
            else:  # Box is not locked.
                candyCnt += candies[box]
                currBoxes.extend(containedBoxes[box])
                collectedKeys |= set(keys[box])

            visited.add(box)

        return candyCnt


status = [1, 0, 1, 0]
candies = [7, 5, 4, 100]
keys = [[], [], [1], []]
containedBoxes = [[1, 2], [3], [], []]
initialBoxes = [0]
print(Solution().maxCandies(status, candies, keys, containedBoxes, initialBoxes))
