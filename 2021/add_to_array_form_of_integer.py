"""
https://leetcode.com/problems/add-to-array-form-of-integer/
"""


class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        for i in range(len(num) - 1, -1, -1):
            if not k:
                break

            k, num[i] = divmod(num[i] + k, 10)

        if k:
            num = list(map(int, str(k))) + num

        return num


print(Solution().addToArrayForm([1, 2, 0, 0], 34))
