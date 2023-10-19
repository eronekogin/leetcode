"""
https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/
"""


class Solution:
    """
    Solution.
    """

    def smallest_missing_value_subtree(self, parents: list[int], nums: list[int]) -> list[int]:
        """
        smallest_missing_value_subtree
        """
        def dfs(i: int):
            if seen[nums[i]] == 0:
                for j in children[i]:
                    dfs(j)

                seen[nums[i]] = 1

        n = len(parents)
        rslt = [1] * n
        if 1 not in nums:
            return rslt

        # Maximum missing genetic value could be n + 1.
        seen = [0] * (10 ** 5 + 2)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parents[i]].append(i)

        i = nums.index(1)
        miss = 1
        while i >= 0:
            dfs(i)
            while seen[miss]:
                miss += 1

            rslt[i] = miss
            i = parents[i]  # Go upper.

        return rslt
