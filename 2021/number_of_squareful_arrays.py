"""
https://leetcode.com/problems/number-of-squareful-arrays/
"""


from collections import Counter


class Solution:
    def numSquarefulPerms(self, nums: list[int]) -> int:
        """
        1. First count the occurrences of each unique number.
        2. Then get all the candidates that could form a perfect square for
            each unique number.
        3. Then dfs and back tracking to get the number of permutations.
        """
        def isSumSquare(x: int, y: int) -> int:
            return int((x + y) ** 0.5) ** 2 == (x + y)

        def dfs(currNum: int, left: int = len(nums) - 1) -> int:
            cnt[currNum] -= 1

            if left:
                count = sum(
                    dfs(nextNum, left - 1)
                    for nextNum in candidates[currNum]
                    if cnt[nextNum]
                )
            else:
                count = 1

            cnt[currNum] += 1
            return count

        cnt = Counter(nums)
        candidates = {i: {j for j in cnt if isSumSquare(i, j)} for i in cnt}
        return sum(map(dfs, cnt))
