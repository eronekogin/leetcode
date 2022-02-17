"""
https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
"""


from collections import Counter


class Solution:
    def isPossibleDivide(self, nums: list[int], k: int) -> bool:
        cnt = Counter(nums)
        while cnt:
            minNum = min(cnt.keys())
            for num in range(minNum, minNum + k):
                if num not in cnt:
                    return False

                cnt[num] -= 1
                if not cnt[num]:
                    del cnt[num]

        return True


print(Solution().isPossibleDivide([1, 2, 3, 3, 4, 4, 5, 6], 4))
