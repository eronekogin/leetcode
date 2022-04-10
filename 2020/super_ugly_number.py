"""
https://leetcode.com/problems/super-ugly-number/
"""


from typing import List
import heapq


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        pLen = len(primes)
        idxs, vals, nums = [0] * pLen, primes[:], [1] * n
        for i in range(1, n):
            nums[i] = num = min(vals)
            for j, val in enumerate(vals):
                if num == val:
                    idxs[j] += 1
                    vals[j] = nums[idxs[j]] * primes[j]

        return nums[-1]

    def nthSuperUglyNumber2(self, n: int, primes: List[int]) -> int:
        """
        Use heaq to get the minimum value in logn time.
        We provide a list of generators to heapq.merge, so that it will return
        a generator of integers. Each time this generator is called, it will
        try to call the next method of any of its generators if its value is
        not currently visable, otherwise it will simply use the previously
        pulled value. Then it compares those values use heap sort and return
        the smallest integer from them. In our case it is the next ugly number.

        Make sure to handle the duplicate case.
        """
        uglies = [1]

        def gen_ugly(prime: int) -> int:
            for ugly in uglies:
                yield ugly * prime

        for ugly in heapq.merge(*map(gen_ugly, primes)):
            if len(uglies) == n:
                return uglies[-1]

            if ugly != uglies[-1]:  # Handle duplicates.
                uglies.append(ugly)
