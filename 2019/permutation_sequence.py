"""
https://leetcode.com/problems/permutation-sequence/
"""


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        Group all permutations by its leading number, then for each group,
        there will be (n-1)! elements. Then for each sub groups, there will be
        (n-2)!, (n-3)!, etc. So use k and n to calculate which group the kth
        element will fall into.
        """
        numStack = [str(i) for i in range(1, n + 1)]
        nextK = k - 1
        rslt = []
        subTotal = 1
        for i in range(2, n):  # Calculate (n-1)!.
            subTotal *= i

        for nextN in range(n - 1, 0, -1):
            # Get the number on the current position.
            i, nextK = divmod(nextK, subTotal)
            rslt.append(numStack.pop(i))
            subTotal //= nextN

        # Add the last element.
        rslt.append(numStack.pop())
        return ''.join(rslt)


print(Solution().getPermutation(4, 3))
