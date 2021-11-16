"""
https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/
"""


class Solution:
    def mctFromLeafValues(self, arr: list[int]) -> int:
        """
        1. Two leaf node a, b could form a non-leaf node. Suppose a <= b, then
            a will not be used any longer in the upper level to form new
            non-leaf node, as it is out numbered by b.
        2. So the problem could be translated as: given a list A, choose any
            two neighbors a and b and remove the smaller one from (a, b) with
            cost a * b, try to find the smallest sum of such cost until the
            array has only 1 item left.
        3. In order to keep cost minimum, b has two candidates: either the
            first bigger number on the left, or the first bigger number on the
            right.
        4. Then it can be further reduced to find the next greater element in
            the array.
        """
        cost = 0
        stack = [float('inf')]
        for node in arr:
            while stack[-1] <= node:
                mid = stack.pop()

                # currNode * min(left, right)
                cost += mid * min(stack[-1], node)

            stack.append(node)

        while len(stack) > 2:
            cost += stack.pop() * stack[-1]

        return cost
