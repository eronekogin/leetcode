"""
https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/

https://github.com/eronekogin/leetcode/blob/master/pics/k_th_smallest_in_lexicographical_order.png
"""


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        """
        Take the lexicographical order list as a tree whose node contains 10
        children from 0 to 9.
        """
        currNum, remainSteps = 1, k - 1
        while remainSteps:
            # Calculate the total steps we need to walk from the currNum node
            # to the currNum + 1 node.
            neededSteps = 0
            src, dst = currNum, currNum + 1
            while src <= n:
                neededSteps += min(n + 1, dst) - src
                src *= 10
                dst *= 10

            if neededSteps <= remainSteps:
                # Continue to walk to the next node on the same level.
                currNum += 1
                remainSteps -= neededSteps
            else:  # Continue to go to the next level.
                currNum *= 10
                remainSteps -= 1

        return currNum


print(Solution().findKthNumber(10, 3))
