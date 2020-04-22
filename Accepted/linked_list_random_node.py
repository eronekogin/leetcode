"""
https://leetcode.com/problems/linked-list-random-node/
"""


from test_helper import ListNode
from random import random


class Solution:

    def __init__(self, head: ListNode):
        self.head = head

    def getRandom(self) -> int:
        """
        Use reservoir sampling algorithm as follows:

        Suppose n is the total length of the list, then we have:
        1. n = 1, probability = 1.

        2. n = 2, probability = 1/2.

        3. n = 3, we generate a random number between (0, 1), if it is
        less than 1/3, we return the third number, otherwise, we return
        the selected number from step 2. So the probability of the third
        number is 1/3 while the probabilty of the previous two numbers is
        1/2 * (1 - 1/3) = 1/3, which means they are selected with the same
        probability.

        4. Assume n = m, probability = 1/m.

        5. Then when n = m + 1, the probability of selecting the previous
        numbers is 1/m * (1 - 1/(m+1)) = 1/(m + 1).

        So with this solution, the probability of each selected number is 1/n.
        """
        currNode = self.head
        totalNodes = 1
        prePicked = None
        while currNode:
            if random() < 1 / totalNodes:
                prePicked = currNode.val

            currNode = currNode.next
            totalNodes += 1

        return prePicked
