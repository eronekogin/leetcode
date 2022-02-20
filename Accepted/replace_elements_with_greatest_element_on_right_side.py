"""
https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
"""


class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        currMax = nextMax = arr[-1]
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] > currMax:
                nextMax = arr[i]

            arr[i] = currMax
            currMax = nextMax

        arr[-1] = -1
        return arr


print(Solution().replaceElements([17, 18, 5, 4, 6, 1]))
