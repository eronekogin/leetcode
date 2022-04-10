"""
https://leetcode.com/problems/split-array-into-consecutive-subsequences/
"""


from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # p1, p2, p3 stands for the number of consecutive subsequences ending
        # at pre with length 1, 2 and >= 3. Similar as c1, c2, c3.
        p1 = p2 = p3 = c1 = c2 = c3 = 0
        i, n, prev = 0, len(nums), nums[0] - 2
        while i < n:
            curr = nums[i]
            cnt = 1  # The number of duplicates of the current number.
            while i + 1 < n and nums[i + 1] == nums[i]:
                cnt += 1
                i += 1

            if curr != prev + 1:
                # When previously having consecutive subsequences with length
                # 1 and 2, we cannot append any following numbers to those
                # subsequences to make them longer, which fails the split.
                if p1 or p2:
                    return False

                c1, c2, c3 = cnt, 0, 0
            else:
                # When we don't have enough current number to be appended to
                # the previously existing short subsequences, the split fails.
                if cnt < p1 + p2:
                    return False

                c2 = p1  # length 1 -> length 2.
                c3 = p2 + min(p3, cnt - p1 - p2)  # length 2 -> length >= 3.
                c1 = max(0, cnt - p1 - p2 - p3)

            prev, p1, p2, p3 = curr, c1, c2, c3
            i += 1

        return not (p1 or p2)  # No short subsequences in the end.


print(Solution().isPossible([1, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
