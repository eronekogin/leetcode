"""
https://leetcode.com/problems/delete-columns-to-make-sorted-ii/
"""


class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        deleteCnt = 0
        R, C = len(strs), len(strs[0])
        remainUnsorted = set(range(R - 1))
        for c in range(C):
            if any(strs[r][c] > strs[r + 1][c] for r in remainUnsorted):
                # The current column is not sorted.
                deleteCnt += 1
            else:
                # Part of the current column is sorted, record the places
                # where str[r][c] == str[r + 1][c] to be determined by the
                # next round check.
                remainUnsorted -= set(
                    r
                    for r in remainUnsorted
                    if strs[r][c] < strs[r + 1][c]
                )

        return deleteCnt


print(Solution().minDeletionSize(["xga", "xfb", "yfa"]))
