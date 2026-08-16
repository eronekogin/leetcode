"""
https://leetcode.com/problems/maximum-total-damage-with-spell-casting/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def maximum_total_damage(self, power: list[int]) -> int:
        """
        maximum total damage
        """
        cnt = Counter(power)
        candidates = [(-10 ** 9, 0)]

        for k in sorted(cnt.keys()):
            candidates.append((k, cnt[k]))

        n = len(candidates)
        dp = [0] * n
        max_damage = 0
        start = 1
        for end in range(1, n):
            curr_power, freq = candidates[end]
            while start < end and candidates[start][0] < curr_power - 2:
                max_damage = max(max_damage, dp[start])
                start += 1

            dp[end] = max_damage + curr_power * freq

        return max(dp)


print(Solution().maximum_total_damage([1, 1, 3, 4]))
