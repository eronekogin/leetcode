"""
https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/description/
"""


class Solution:
    """
    Solution
    """

    def min_number_of_hours(
        self,
        initial_energy: int,
        initial_experience: int,
        energy: list[int],
        experience: list[int]
    ) -> int:
        """
        min number of hours
        """
        needed = 0
        curr_e, curr_exp = initial_energy, initial_experience
        for e, exp in zip(energy, experience):
            if curr_e > e:
                curr_e -= e
            else:
                needed += e - curr_e + 1
                curr_e = 1

            if curr_exp <= exp:
                delta = exp - curr_exp + 1
                needed += delta
                curr_exp += delta

            curr_exp += exp

        return needed


print(Solution().min_number_of_hours(1, 1, [1, 1, 1, 1], [1, 1, 1, 50]))
