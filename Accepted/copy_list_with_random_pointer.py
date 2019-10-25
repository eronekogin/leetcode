"""
https://leetcode.com/problems/copy-list-with-random-pointer/
"""


from test_helper import RandomNode
from collections import defaultdict


class Solution:
    def copyRandomList(self, head: RandomNode) -> RandomNode:
        visited = defaultdict(lambda: RandomNode(None, None, None))
        visited[None] = None
        currNode = head
        while currNode:
            visited[currNode].val = currNode.val
            visited[currNode].next = visited[currNode.next]
            visited[currNode].random = visited[currNode.random]
            currNode = currNode.next

        return visited[head]


a, b = RandomNode(1, None, None), RandomNode(2, None, None)
a.next = b
a.random = b
b.random = b
print(Solution().copyRandomList(a))
