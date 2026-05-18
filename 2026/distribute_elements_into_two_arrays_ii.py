"""
https://leetcode.com/problems/distribute-elements-into-two-arrays-ii/description/
"""

from sortedcontainers import SortedList


class Solution:
    """
    Solution
    """

    def result_array(self, nums: list[int]) -> list[int]:
        """
        result array
        """
        def greater_counter(values: SortedList, target: int) -> int:
            return len(values) - values.bisect_right(target)

        def add(v: list[int], sv: SortedList, target: int) -> None:
            v.append(target)
            sv.add(target)

        a1 = [nums[0]]
        sa1 = SortedList([nums[0]])
        a2 = [nums[1]]
        sa2 = SortedList([nums[1]])

        for i in range(2, len(nums)):
            x = nums[i]
            g1 = greater_counter(sa1, x)
            g2 = greater_counter(sa2, x)

            if g1 > g2:
                add(a1, sa1, x)
            elif g1 < g2:
                add(a2, sa2, x)
            elif len(a1) < len(a2):
                add(a1, sa1, x)
            elif len(a1) > len(a2):
                add(a2, sa2, x)
            else:
                add(a1, sa1, x)

        return a1 + a2


print(Solution().result_array([2, 1, 3, 3]))
