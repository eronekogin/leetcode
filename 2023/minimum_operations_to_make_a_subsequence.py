"""
https://leetcode.com/problems/minimum-operations-to-make-a-subsequence/
"""


from bisect import bisect_left


class Solution:
    def minOperations(self, target: list[int], arr: list[int]) -> int:
        """
        1. Since "target" array has distinct elements that means I can give
            every element an index which is unique to it.
        2. Now let us delete all the elements in "arr" array which are not
            present in the target array.
        3. What is left in "arr" array is all the elements which are present
            in target.
        4. Replace each element in "arr" with its index from target array.
            What that means is if you have element "5" in arr and its index
            is 1 in target array then, you replace the element with that index.
        5. Now you have indexes instead of elements.
        6. Now you find the longest incresing subseqence. Why increasing?
            because remember the indexing the target array is
            0,1,2,3,4,5,... so on.
        """
        orders = {x: i for i, x in enumerate(target)}
        stack = []
        for x in arr:
            if x not in orders:
                continue

            i = bisect_left(stack, orders[x])
            if i == len(stack):
                stack.append(0)

            stack[i] = orders[x]

        return len(target) - len(stack)
