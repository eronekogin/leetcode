"""
https://leetcode.com/problems/find-latest-group-of-size-m/
"""


class Solution:
    def findLatestStep(self, arr: list[int], m: int) -> int:
        n = len(arr)
        if n == m:
            return len(arr)

        currGroups = [(0, len(arr) - 1)]
        for step in range(n - 1, 0, -1):
            if not currGroups:  # Not enough length of group to split.
                return -1

            splitIndex = arr[step] - 1
            nextGroups: list[tuple[int]] = []
            for start, end in currGroups:
                if start <= splitIndex <= end:
                    if splitIndex - start == m:
                        return step
                    elif splitIndex - start > m:
                        nextGroups.append((start, splitIndex - 1))

                    if end - splitIndex == m:
                        return step
                    elif end - splitIndex > m:
                        nextGroups.append((splitIndex + 1, end))
                else:
                    nextGroups.append((start, end))

            currGroups = nextGroups


print(Solution().findLatestStep([1, 9, 12, 6, 4, 5, 3, 13, 2, 11, 10, 7, 8],
                                4))
