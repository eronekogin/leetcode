"""
https://leetcode.com/problems/largest-values-from-labels/
"""


from collections import Counter


class Solution:
    def largestValsFromLabels(
        self,
        values: list[int],
        labels: list[int],
        numWanted: int,
        useLimit: int
    ) -> int:
        sortedItems = sorted(zip(values, labels), key=lambda x: -x[0])
        usedLabels = Counter()
        score = 0
        total = 0
        for value, label in sortedItems:
            if total < numWanted:  # Want more item.
                if usedLabels[label] < useLimit:  # Label is still available.
                    score += value
                    usedLabels[label] += 1
                    total += 1
            else:
                break

        return score


print(Solution().largestValsFromLabels([5, 4, 3, 2, 1],
                                       [1, 1, 2, 2, 3],
                                       3,
                                       1))
