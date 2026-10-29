"""
https://leetcode.com/problems/minimum-amount-of-damage-dealt-to-bob/description/
"""


from functools import cmp_to_key


class Solution:
    """
    Solution
    """
    def min_damage(self, power: int, damage: list[int], health: list[int]) -> int:
        """
        min damage
        """
        n = len(damage)
        time: list[int] = [0] * n

        for i in range(n):
            time[i] = (health[i] + power - 1) // power

        kill_order = sorted(
            range(n),
            key=cmp_to_key(lambda i, j: time[i] * damage[j] - time[j] * damage[i])
        )

        curr_time = 0
        rslt = 0
        for i in kill_order:
            curr_time += time[i]
            rslt += curr_time * damage[i]

        return rslt

print(Solution().min_damage(62, [80, 79], [86, 13]))
