"""
https://leetcode.com/problems/recover-the-original-array/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def recover_array(self, nums: list[int]) -> list[int]:
        """
        recover_array
        """
        def check(cnt: Counter, double_k: int):
            rslt = []
            k = double_k >> 1
            for x in sorted_nums:
                if cnt[x] == 0:
                    continue

                if cnt[x + double_k] == 0:
                    return (False, [])

                cnt[x] -= 1
                cnt[x + double_k] -= 1

                rslt.append(x + k)

            return (True, rslt)

        sorted_nums = sorted(nums)
        cnt = Counter(sorted_nums)
        n = len(nums) >> 1
        for i in range(1, n + 1):
            double_k = sorted_nums[i] - sorted_nums[0]
            if double_k <= 0 or double_k & 1:
                continue

            is_found, rslt = check(cnt.copy(), double_k)
            if is_found:
                return rslt

        return []


print(Solution().recover_array([2, 10, 6, 4, 8, 12]))
