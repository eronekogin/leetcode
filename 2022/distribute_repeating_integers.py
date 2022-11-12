"""
https://leetcode.com/problems/distribute-repeating-integers/
"""


from collections import Counter


class Solution:
    def canDistribute(self, nums: list[int], quantity: list[int]) -> bool:
        def dfs(customer: int):
            if customer == len(quantity):
                return True

            for i in range(len(left)):
                if left[i] >= quantity[customer]:
                    left[i] -= quantity[customer]
                    if dfs(customer + 1):
                        return True

                    left[i] += quantity[customer]

            return False

        cnt = Counter(nums)
        m = len(quantity)
        left = sorted(cnt.values())[-m:]
        quantity.sort(reverse=True)
        return dfs(0)
