"""
https://leetcode.com/problems/split-the-array-to-make-coprime-products/description/
"""

MAX_NUM = 10 ** 6
spf = list(range(MAX_NUM + 1))
for i in range(2, int(MAX_NUM ** 0.5) + 1):
    if spf[i] == i:
        for j in range(i * i, MAX_NUM + 1, i):
            spf[j] = min(spf[j], i)


def get_primes(x: int):
    """
    get primes
    """
    while x > 1:
        yield spf[x]
        x //= spf[x]


class Solution:
    """
    Solution
    """

    def find_valid_split(self, nums: list[int]) -> int:
        """
        find valid split
        """
        rightmost_indexes: dict[int, int] = {}
        for k, x in enumerate(nums):
            for p in get_primes(x):
                rightmost_indexes[p] = k

        split_index = 0
        for k in range(len(nums) - 1):
            for p in get_primes(nums[k]):
                split_index = max(split_index, rightmost_indexes[p])

            if split_index == k:
                return split_index

        return -1


print(Solution().find_valid_split([1, 1, 89]))
