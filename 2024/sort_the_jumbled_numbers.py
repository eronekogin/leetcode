"""
https://leetcode.com/problems/sort-the-jumbled-numbers/description/
"""


class Solution:
    """
    Solution
    """

    def sort_jumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        """
        sort jumbled
        """
        def transfer(x: int):
            if x == 0:
                return mapping[0]

            curr_num = x
            digits: list[int] = []
            while curr_num > 0:
                curr_num, r = divmod(curr_num, 10)
                digits.append(mapping[r])

            new_num = 0
            for num in reversed(digits):
                new_num = new_num * 10 + num

            return new_num

        return sorted(nums, key=transfer)


print(Solution().sort_jumbled([8, 9, 4, 0, 2, 1, 3, 5, 7, 6], [991, 338, 38]))
