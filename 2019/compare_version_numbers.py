"""
https://leetcode.com/problems/compare-version-numbers/
"""


from typing import List
from itertools import zip_longest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        for v1, v2 in zip_longest(
                self.decompose_version(version1),
                self.decompose_version(version2),
                fillvalue=0):
            if v1 > v2:
                return 1

            if v1 < v2:
                return -1

        return 0

    def decompose_version(self, version: str) -> List[int]:
        return [int(_) for _ in version.split('.')]
