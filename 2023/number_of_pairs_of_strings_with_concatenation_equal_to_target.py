"""
https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def num_of_pairs(self, nums: list[str], target: str) -> int:
        """
        num_of_pairs
        """
        cnt = Counter(nums)
        rslt = 0
        for key in cnt:
            offset = len(key)
            if key != target[:offset]:
                continue

            remain = target[offset:]
            if key == remain:
                rslt += cnt[key] * (cnt[key] - 1)
            else:
                rslt += cnt[key] * cnt[remain]

        return rslt


print(Solution().num_of_pairs(["9", "93", "9", "2", "32", "32"], '932'))
