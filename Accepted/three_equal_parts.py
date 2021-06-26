"""
https://leetcode.com/problems/three-equal-parts/
"""


class Solution:
    def threeEqualParts(self, arr: list[int]) -> list[int]:
        NOT_FOUND = [-1, -1]
        s = sum(arr)
        onesInEachPart, r = divmod(s, 3)
        if r:  # Must have equal ones in each part.
            return NOT_FOUND

        if not onesInEachPart:  # arr is all zeros.
            return [0, len(arr) - 1]

        breakIndexes = []
        breakCheck1 = {1, onesInEachPart + 1, 2 * onesInEachPart + 1}
        breakCheck2 = {onesInEachPart, 2 * onesInEachPart, 3 * onesInEachPart}
        onesCnt = 0
        for i, x in enumerate(arr):
            if x:
                onesCnt += 1
                if onesCnt in breakCheck1:
                    breakIndexes.append(i)

                if onesCnt in breakCheck2:
                    breakIndexes.append(i)

        i1, j1, i2, j2, i3, j3 = breakIndexes
        if not (arr[i1: j1 + 1] == arr[i2: j2 + 1] == arr[i3: j3 + 1]):
            return NOT_FOUND

        # Check zeros after j1, j2, j3.
        x, y, z = i2 - j1 - 1, i3 - j2 - 1, len(arr) - j3 - 1
        if x < z or y < z:  # Not enough zeros in the first two parts.
            return NOT_FOUND

        return [j1 + z, j2 + z + 1]  # Fill up necessary zeros.


print(Solution().threeEqualParts([1, 0, 1, 0, 1]))
