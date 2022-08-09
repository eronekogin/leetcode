"""
https://leetcode.com/problems/find-a-value-of-a-mysterious-function-closest-to-target/
"""


class Solution:
    def closestToTarget(self, arr: list[int], target: int) -> int:
        """
        1. Suppose a1 = arr[i], a2 = arr[i] & arr[i + 1], a3 = ..., we have
            a1 >= a2 >= a3, as AND operation does not set any bit, so either
            the 1 bit becomes zero, or to remain 1 bit.
        2. subArrayAnds[i] = arr[i] & subArrayAnds[i + 1].
        3. suppose and[i:j] stands for the and values of subarray starting at
            index i with length j, then we have: 
                and[i:j]
                    = arr[i] & and[i+1:j-1]
                    = arr[i] & arr[i+1] & and[i+2:j-2]
                    = arr[i] & arr[i+1] & arr[i+2] & and[i+3:j-3]
                    = ...
            Eventually all the and[i:j] will be inside subArrayAnds.
        4. So we could just iterate on subArrayAnds and check the absolute
            value of subArrayAnd - target for each subArrayAnd.
        """
        N = len(arr)
        subArrayAnds: list[set[int]] = [set() for _ in range(N)]
        subArrayAnds[-1].add(arr[-1])

        # Calculate sub array ands.
        for i in range(N - 2, -1, -1):
            subArrayAnds[i].add(arr[i])
            for val in subArrayAnds[i + 1]:
                subArrayAnds[i].add(arr[i] & val)

        # Calculate result.
        rslt = float('inf')
        for subArrayAnd in subArrayAnds:
            for val in subArrayAnd:
                rslt = min(rslt, abs(val - target))

        return rslt
