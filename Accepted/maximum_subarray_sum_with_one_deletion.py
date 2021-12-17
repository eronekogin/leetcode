"""
https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/
"""


class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        N = len(arr)
        withoutDeletes = [arr[0]] * N
        withDeletes = [arr[0]] * N
        result = arr[0]
        for i in range(1, N):
            withoutDeletes[i] = max(withoutDeletes[i - 1] + arr[i], arr[i])
            withDeletes[i] = max(withDeletes[i - 1] + arr[i], arr[i])
            if i >= 2:
                withDeletes[i] = max(
                    withDeletes[i], withoutDeletes[i - 2] + arr[i])

            result = max(result, withDeletes[i])

        return result


print(Solution().maximumSum([-1, -1, -1, -1]))
