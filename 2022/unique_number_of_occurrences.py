"""
https://leetcode.com/problems/unique-number-of-occurrences/
"""


from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        occurrences = Counter(arr).values()
        return len(set(occurrences)) == len(occurrences)
