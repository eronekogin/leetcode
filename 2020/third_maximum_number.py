"""
https://leetcode.com/problems/third-maximum-number/
"""


from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        top3 = set()
        for num in nums:
            top3.add(num)
            if len(top3) > 3:
                top3.remove(min(top3))

        if len(top3) < 3:
            return max(top3)

        return min(top3)


print(Solution().thirdMax([1, 2, 2]))
