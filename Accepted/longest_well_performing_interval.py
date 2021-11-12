"""
https://leetcode.com/problems/longest-well-performing-interval/
"""


class Solution:
    def longestWPI(self, hours: list[int]) -> int:
        """
        1. seen records the first occurrence of a new score.
        2. If current score > 0, the subarray from 0 to i satisfied the
            condition, so the total length so far is i + 1.
        3. Else, we want to find an index j, whose score was score - 1, then
            from j to i, the total score is 1, which satisfied the condition.
        4. The reason why we don't choose score - 2, score - 3, ..., score -x
            where x is greather than 1 is because we were always recording
            the new score where it first occurrred. So score - x must come
            later than score -1, which means it will stay at a nearer place
            to i comparing with score - 1. So we just need to find score - 1
            instead.
        5. If no such score - 1, continue to scan the remaininng items.
        """
        maxLen = score = 0
        seen: dict[int, int] = {}
        for i, h in enumerate(hours):
            if h > 8:
                score += 1
            else:
                score -= 1

            if score > 0:
                maxLen = i + 1

            seen.setdefault(score, i)
            if score - 1 in seen:
                maxLen = max(maxLen, i - seen[score - 1])

        return maxLen


print(Solution().longestWPI([9, 9, 6, 0, 6, 6, 9]))
