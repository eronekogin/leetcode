"""
https://leetcode.com/problems/can-place-flowers/
"""


from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        availablePlaces, i, total = 0, 0, len(flowerbed) - 1
        while i < total:
            if not flowerbed[i]:
                if not flowerbed[i + 1]:
                    availablePlaces += 1
                    if availablePlaces >= n:
                        return True
                else:  # Skip to the next place.
                    i += 1

            i += 2

        if i == total:  # Just falling to the last position.
            availablePlaces += flowerbed[i] == 0

        return n <= availablePlaces


print(Solution().canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2))
