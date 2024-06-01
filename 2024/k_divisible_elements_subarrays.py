"""
https://leetcode.com/problems/k-divisible-elements-subarrays/description/
"""


class Solution:
    """
    Solution
    """

    def count_distinct(self, nums: list[int], k: int, p: int) -> int:
        """
        count distinct
        """
        trie = {}
        n = len(nums)
        rslt = 0

        for start in range(n):
            cnt = 0
            curr = trie

            for end in range(start, n):
                num = nums[end]
                cnt += num % p == 0

                if cnt > k:
                    break

                if num not in curr:
                    curr[num] = {}
                    rslt += 1

                curr = curr[num]

        return rslt
