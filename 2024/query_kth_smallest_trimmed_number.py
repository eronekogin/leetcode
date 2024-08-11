"""
https://leetcode.com/problems/query-kth-smallest-trimmed-number/description/
"""


class Solution:
    """
    Solution
    """

    def smallest_trimmed_numbers(self, nums: list[str], queries: list[list[int]]) -> list[int]:
        """
        smallest trimmed numbers
        """
        def perform_query(k: int, t: int) -> int:
            trimmed_nums = [x[len(x) - t:] for x in nums]
            return sorted((x, i) for i, x in enumerate(trimmed_nums))[k - 1][1]

        return [perform_query(*q) for q in queries]

    def smallest_trimmed_numbers2(self, nums: list[str], queries: list[list[int]]) -> list[int]:
        """
        use radix sort
        """
        m, n = len(nums), len(nums[0])

        ranks = [list(range(m))]

        # Sort from the last digit to the first to keep the relative order based on
        # the previous digit.
        for i in range(n - 1, -1, -1):
            prev_rank = {x: j for j, x in enumerate(ranks[-1])}

            ranks.append(
                sorted(
                    range(m),
                    key=lambda x: (nums[x][i], prev_rank[x])
                )
            )

        return [ranks[t][k - 1] for k, t in queries]


print(Solution().smallest_trimmed_numbers2(
    ["9415", "5908", "1840", "5307"], [[3, 2], [2, 2], [3, 3], [1, 3]]))
