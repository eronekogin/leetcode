"""
https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
"""


class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        def is_enough_bouquests(mid: int) -> bool:
            bouquest = 0
            totalConsecutiveFlowers = 0
            for b in bloomDay:
                if b > mid:
                    totalConsecutiveFlowers = 0
                else:
                    totalConsecutiveFlowers += 1

                if totalConsecutiveFlowers >= k:
                    totalConsecutiveFlowers = 0
                    bouquest += 1

                    if bouquest == m:  # Got enough bouquests
                        return True

            return False

        n = len(bloomDay)
        if m * k > n:  # Not enough flowers.
            return -1

        l, r = 1, 10 ** 9
        while l < r:
            mid = l + ((r - l) >> 1)
            if is_enough_bouquests(mid):  # Need less or same flowers.
                r = mid
            else:  # Need more flowers.
                l = mid + 1

        return l
