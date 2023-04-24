"""
https://leetcode.com/problems/count-nice-pairs-in-an-array/
"""


from collections import Counter


class Solution:
    def countNicePairs(self, nums: list[int]) -> int:
        """
        nums[i] + revs[j] = nums[j] + revs[i] ==>
        nums[i] - revs[i] = nums[j] - revs[j] ==>
        Then we just need to find how many pairs having the same difference.
        """
        pairs = 0
        cnt = Counter()
        for x in nums:
            y = int(str(x)[::-1])
            pairs += cnt[x - y]
            cnt[x - y] += 1

        return pairs % (10 ** 9 + 7)


print(Solution().countNicePairs([42, 11, 1, 97]))
