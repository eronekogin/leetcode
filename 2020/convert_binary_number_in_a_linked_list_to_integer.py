"""
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
"""


from test_helper import ListNode


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        currHead, rslt = head, 0
        while currHead:
            rslt = (rslt << 1) + currHead.val
            currHead = currHead.next

        return rslt
