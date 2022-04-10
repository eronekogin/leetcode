"""
https://leetcode.com/problems/sliding-window-median/
"""


from typing import List
from heapq import heappush, heappop
from collections import defaultdict


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def get_median() -> float:
            if k & 1:  # k is odd.
                return float(largers[0])

            return (largers[0] - smallers[0]) / 2

        smallers, largers = [], []
        discards = defaultdict(int)  # number: total count to be deleted.

        # Initialize two heaps from the first k items in nums.
        for i in range(k):
            heappush(smallers, -nums[i])

        for i in range((k + 1) >> 1):
            heappush(largers, -heappop(smallers))

        medians = [get_median()]

        for end in range(k, len(nums)):
            discard, add, balance = nums[end - k], nums[end], 0

            # Calculate balance change based on the number to be deleted.
            if smallers and discard <= -smallers[0]:
                balance += 1  # Towards largers.
                if discard == -smallers[0]:
                    heappop(smallers)
                else:
                    discards[discard] += 1
            else:
                balance -= 1  # Towards smallers.
                if discard == largers[0]:
                    heappop(largers)
                else:
                    discards[discard] += 1

            # Calculate balance change based on the number to be added.
            if smallers and add <= -smallers[0]:
                balance -= 1  # Towards smallers.
                heappush(smallers, -add)
            else:
                balance += 1  # Towards largers.
                heappush(largers, add)

            # Rebalance the two heaps.
            if balance < 0:  # Too many numbers in the smallers.
                heappush(largers, -heappop(smallers))
            elif balance > 0:  # Too many numbers in the largers.
                heappush(smallers, -heappop(largers))

            # Remove the numbers which need to be discarded when they are
            # on the top of each heap.
            while smallers and discards[-smallers[0]]:
                discards[-heappop(smallers)] -= 1

            while largers and discards[largers[0]]:
                discards[heappop(largers)] -= 1

            medians.append(get_median())

        return medians


print(Solution().medianSlidingWindow([7, 0, 3, 9, 9, 9, 1, 7, 2, 3], 6))
