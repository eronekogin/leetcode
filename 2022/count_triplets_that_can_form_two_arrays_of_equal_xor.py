"""
https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/
"""


class Solution:
    def countTriplets(self, arr: list[int]) -> int:
        """
        1. if the prefix xor at index i is a, and if the prefix xor at index k
            is a when i < k, then the xor among the elements withing i to k
            is zero. j could occur in any position among i to k except at
            index i, so the total combination for this group is
            len(i to k) - 1 = k - (i + 1) + 1 - 1 = k - i - 1
        2. Then we simply count the prefix xor, and for each xor that occurred
            before, suppose the current index is k, then the total combinations
            are:
            k - i1 - 1 + k - i2 - 1 + k - i3 - 1 = k * 3 - (i1 + i2 + i3) - 3
        3. So in general, we have:
            k * n - (i1 + ... + in) - n
        """
        cnt = currXor = 0
        memo = {0: [1, 0]}  # xor: [freq, sum of previous occurrence index]
        for k, num in enumerate(arr):
            currXor ^= num
            freq, totalIndexSum = memo.get(currXor, [0, 0])
            cnt += k * freq - totalIndexSum
            memo[currXor] = [freq + 1, totalIndexSum + k + 1]

        return cnt
