"""
https://leetcode.com/problems/count-the-number-of-inversions/description/
"""


class Solution:
    """
    Solution
    """

    def number_of_permutations(self, n: int, requirements: list[list[int]]) -> int:
        """
        number of permutations
        """
        memo = {e: c for e, c in requirements}
        max_req = max(memo.values())
        max_end = max(memo.keys())
        m = 10 ** 9 + 7

        # dp[i] stands for the number of inversions from [0...i], inclusively
        dp = [1] + [0] * max_req

        # Check requirements
        for e in range(max_end + 1):
            dp2 = [0] * (1 + max_req)

            if e in memo:
                c = memo[e]
                # dp2[c] has a requirement, and to add a new element e to
                # the previous permutations, it can add at most e inversions
                # from right to far left positions
                dp2[c] = sum(dp[max(0, c - e): c + 1]) % m
            else:
                # dp2[c] has no requirement, so adding the new element e to
                # the previous permutation is like a sliding window, we
                # remove the left most element dp[i - e - 1] and add dp[e]
                for i in range(max_req + 1):
                    dp2[i] = dp[i]
                    if i > 0:
                        dp2[i] += dp2[i - 1]

                    if i > e:
                        dp2[i] -= dp[i - e - 1]

            dp = dp2

        # Check from max_end + 1 to n.
        rslt = sum(dp) % m
        for e in range(max_end + 1, n):
            # For any new added element, it has e + 1 possible insert position
            # to form a valid permutation since no requirement on this index
            rslt = (rslt * (e + 1)) % m

        return rslt
