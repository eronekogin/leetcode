"""
https://leetcode.com/problems/maximum-total-reward-using-operations-i/description/
"""


class Solution:
    """
    Solution
    """

    def max_total_reward(self, reward_values: list[int]) -> int:
        """
        max total reward
        """
        reward_values.sort()

        rslt = {0}

        for r in reward_values:
            new_rewards = set()
            for x in rslt:
                if r > x:
                    new_rewards.add(r + x)

            rslt.update(new_rewards)

        return max(rslt)


print(Solution().max_total_reward([1, 6, 4, 3, 2]))
