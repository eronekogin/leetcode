"""
https://leetcode.com/problems/super-washing-machines/
"""


from typing import List


class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        """
        For each wash machine, check how many dresses will pass through it when
        all the wash machines have the same number of dresses:
        1. For the ith machine, its left side's required dresses:
            L = avg * i - sum[:i + 1]
        2. Its right side required dresses:
            R = avg * (n - i - 1) - sum[i + 1:]
        3. If L > 0 and R > 0, it means both sides need to import dresses and
            since each wash machine can only pass out only one dress at a time,
            the total dresses passed through the ith machine is L + R.
        4. If L < 0 and R < 0, it means both sides need to export dresses and
            they can be done at the same time, so the total dresses passed
            through the ith machine is max(L, R)
        5. Otherwise, the import and export on both sides could be done at the
            same time, so the total dresses passed through the ith machine is
            still max(L, R).

        Then our target is to find the maximum dresses passed through on a
        single wash machine among those wash machines.
        """
        total, n = sum(machines), len(machines)
        avg, r = divmod(total, n)
        if r != 0:
            return -1  # Could not be divided equally on each machine.

        l = r = preSum = rslt = 0
        for i in range(n):
            l = avg * i - preSum
            r = avg * (n - i - 1) - (total - preSum - machines[i])
            if l > 0 and r > 0:
                rslt = max(rslt, l + r)
            else:
                rslt = max(rslt, abs(l), abs(r))

            preSum += machines[i]

        return rslt

    def findMinMoves2(self, machines: List[int]) -> int:
        """
        Another way is to think as follows:
        1. Try to find the maximum passed through dresses from the left to the
            right side.
        2. Also try to find the maximum dresses a single wash machine could 
            give out.
        3. Then the maximum move steps we need is between the maximum of the
            above two factors. This is because a wash machine could only give
            out one dress at a time, so we need to take point 2 into
            consideration.
        """
        total, n = sum(machines), len(machines)
        avg, r = divmod(total, n)
        if r != 0:
            return -1  # Could not be divided equally on each machine.

        rslt = passThrough = 0
        for dresses in machines:
            passThrough += dresses - avg

            # Here dresses - avg is the total number of dresses the current
            # wash machine must give out.
            rslt = max(rslt, abs(passThrough), dresses - avg)

        return rslt
