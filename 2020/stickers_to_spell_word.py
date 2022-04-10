"""
https://leetcode.com/problems/stickers-to-spell-word/
"""


from typing import List


from collections import Counter
from math import ceil


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        def pick(usedSteps: int) -> None:
            if usedSteps >= self.minSteps:
                return

            if not candidates:  # Used up all candidate stickers.
                if all(v <= 0 for v in targetCharsCnt.values()):
                    self.minSteps = usedSteps

                return

            s = candidates.pop()  # Pick one candidate sticker.
            maxUsed = max(0, max(ceil(targetCharsCnt[c] / s[c]) for c in s))
            for c in s:  # Calculate remaining target chars.
                targetCharsCnt[c] -= maxUsed * s[c]

            pick(usedSteps + maxUsed)
            for i in range(maxUsed - 1, -1, -1):
                for c in s:
                    targetCharsCnt[c] += s[c]

                pick(usedSteps + i)

            candidates.append(s)  # Append s back for other pick path.

        # Count the chars in each sticker and ignore the chars that are not in
        # the target.
        targetCharsCnt = Counter(target)
        candidates = [Counter(s) & targetCharsCnt for s in stickers]

        # Remove the candidate that is a subset of the other ones.
        for i in range(len(candidates) - 1, -1, -1):
            if any(candidates[i] == (candidates[i] & candidates[j])
                   for j in range(len(candidates)) if i != j):
                candidates.pop(i)

        self.minSteps = len(target) + 1
        pick(0)
        if self.minSteps > len(target):
            return -1

        return self.minSteps


print(Solution().minStickers(
    ["these", "guess", "about", "garden", "him"], "atomher"))
