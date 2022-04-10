"""
https://leetcode.com/problems/linked-list-components/
"""


from test_helper import ListNode


class Solution:
    def numComponents(self, head: ListNode, G: list[int]) -> int:
        cnt = 0
        nodes = set(G)
        currNode = head
        while currNode and nodes:
            nextNode = currNode.next
            if nextNode:
                if currNode.val in nodes and nextNode.val not in nodes:
                    cnt += 1
            elif currNode.val in nodes:
                cnt += 1

            currNode = nextNode

        return cnt


head = ListNode(None).create_node_list(0, 4)
print(Solution().numComponents(head, [0, 1, 3]))
