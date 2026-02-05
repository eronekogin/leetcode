"""
https://leetcode.com/problems/maximum-strong-pair-xor-ii/description/
"""


class Solution:
    """
    Docstring for Solution
    """

    def maximum_strong_pair_xor(self, nums: list[int]) -> int:
        """
        |x - y| <= min(x, y) means if x > y, x - y <= y, so
        it equals to check x <= 2y

        We are building the rslt bit by bit by setting the
        latest bit as 1 as a candidate and check if candidate ^ x
        is available in the prefix set and then apply the above
        restriction
        """
        rslt = 0
        for i in range(20, -1, -1):
            rslt <<= 1  # Add one bit to the result

            # Collect maximum and minimum number in nums
            # that has the current prefix
            prefix1, prefix2 = {}, {}
            for x in nums:
                p = x >> i

                if p not in prefix1:
                    prefix1[p] = x
                    prefix2[p] = x

                prefix1[p] = min(prefix1[p], x)
                prefix2[p] = max(prefix2[p], x)

            # Validate if the current maximum value is achievable
            for px, x in prefix1.items():
                candidate = rslt ^ 1  # set last bit as 1
                py = px ^ candidate

                if px >= py and py in prefix1 and x <= 2 * prefix2[py]:
                    rslt = candidate
                    break

        return rslt
