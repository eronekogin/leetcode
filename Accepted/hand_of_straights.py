"""
https://leetcode.com/problems/hand-of-straights/
"""


from collections import Counter


class Solution:
    def isNStraightHand(self, hand: list[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False

        cnt = Counter(hand)
        while cnt:
            start = min(cnt)
            minCount = cnt[start]
            for end in range(start, start + W):
                if cnt[end] < minCount:
                    return False
                elif cnt[end] == minCount:
                    del cnt[end]
                else:
                    cnt[end] -= minCount

        return True


print(Solution().isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3))
