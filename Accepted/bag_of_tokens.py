"""
https://leetcode.com/problems/bag-of-tokens/
"""


from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        sortedTokens, currPower, currScore, maxScore = sorted(tokens), P, 0, 0
        l, r = 0, len(tokens) - 1
        while l <= r:
            if currPower >= sortedTokens[l]:  # Gain one score from the left.
                currScore += 1
                maxScore = max(maxScore, currScore)
                currPower -= sortedTokens[l]
                l += 1
            elif currScore > 0:  # Gain the curr max power from the right.
                currScore -= 1
                currPower += sortedTokens[r]
                r -= 1
            else:  # Cannot do both.
                break

        return maxScore  # Scanned all.
