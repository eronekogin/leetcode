"""
https://leetcode.com/problems/russian-doll-envelopes/
"""


from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        First sort the input envelopes on the width in ascending and
        height in descending order. This makes sure the width is strictly
        increasing when there is a tie in width, as the descending height
        will eliminate the other cases. For example, [3, 4] could not hold
        [3, 3], so in the sorted result, it will be [3, 4], [3, 3] instead.

        Then try to find the longest increasing subsequence on the height
        to get our final result.
        """
        if not envelopes:
            return 0

        heights = [
            h for _, h in sorted(envelopes, key=lambda x: (x[0], -x[1]))]

        lis = [heights[0]]
        for h in heights:
            if h < lis[0]:
                lis[0] = h
            elif h > lis[-1]:
                lis.append(h)
            else:
                l, r = 0, len(lis) - 1
                while l < r:
                    m = l + ((r - l) >> 1)
                    if lis[m] < h:
                        l = m + 1
                    else:
                        r = m

                lis[l] = h

        return len(lis)


print(Solution().maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]))
