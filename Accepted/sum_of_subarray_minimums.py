"""
https://leetcode.com/problems/sum-of-subarray-minimums/
"""


class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        """
        1. For each number i in arr:
            1.1 Suppose the nearest previous less than i is j, the distance
                between them is m.
            1.2 Suppose the nearest next less than i is k, the distance
                between them is n.
            1.3 Then the total distance between j and k is m + n - 1, the
                number of subarrays between them is
                s1 = 1 + 2 + ... + m + n - 1 = (m + n - 1)(m + n) / 2
            1.4 Then we need to exclude the subarrays that does not contain
                number i, which is composed by the first m - 1 and the last
                n - 1 numbers, so we have:
                s2 = m(m - 1) / 2, s3 = n(n - 1) / 2
            1.5 So the total number of subarrays with minimum number as i is
                s = s1 - s2 - s3 = m * n
        2. Then we use a monostack to calculate the ple and nle list, then
            calculate the result based on the above conclusion.
        """
        N = len(arr)
        monoStack = []
        ple = [i + 1 for i in range(N)]  # PLE = Previous Less Element
        nle = [N - i for i in range(N)]  # NLE = Next less Element
        for i in range(N):
            while monoStack and arr[monoStack[-1]] > arr[i]:
                # Update the distance between monoStack[-1] and i as i
                # could be the NLE for monoStack[-1].
                nle[monoStack[-1]] = i - monoStack[-1]
                monoStack.pop()

            if monoStack:
                # Calculate the distance between i and monoStack[-1] as
                # monoStack[-1] is the PLE for i.
                ple[i] = i - monoStack[-1]

            monoStack.append(i)

        return sum(v * l * r for v, l, r in zip(arr, ple, nle)) % (10 ** 9 + 7)


print(Solution().sumSubarrayMins([3, 1, 2, 4]))
