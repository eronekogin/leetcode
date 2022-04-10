"""
https://leetcode.com/problems/minimum-index-sum-of-two-lists/
"""


from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        memo1 = {s: i for i, s in enumerate(list1)}
        memo2 = {s: i for i, s in enumerate(list2)}
        commons = {s: memo1[s] + memo2[s] for s in memo1 if s in memo2}
        minSum = min(commons.values())
        return [s for s, v in commons.items() if v == minSum]
