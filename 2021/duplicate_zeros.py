"""
https://leetcode.com/problems/duplicate-zeros/
"""


class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        maxLenWithDupZeros = len(arr) - 1
        dupZeros = 0

        # Count possible dup zeros to fit into the new list.
        for left in range(len(arr)):
            if left > maxLenWithDupZeros - dupZeros:
                break

            if arr[left] == 0:
                if left == maxLenWithDupZeros - dupZeros:
                    arr[maxLenWithDupZeros] = 0
                    maxLenWithDupZeros -= 1
                    break

                dupZeros += 1

        lastItemIdx = maxLenWithDupZeros - dupZeros

        # Copy from the last item index to the first item from the original
        # array to the end of the arr.
        for i in range(lastItemIdx, -1, -1):
            if arr[i] == 0:
                arr[i + dupZeros] = 0
                dupZeros -= 1
                arr[i + dupZeros] = 0
            else:
                arr[i + dupZeros] = arr[i]


print(Solution().duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0]))
