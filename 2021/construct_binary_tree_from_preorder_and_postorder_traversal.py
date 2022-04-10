"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/
"""


from test_helper import TreeNode


class Solution:
    def constructFromPrePost(
            self, pre: list[int], post: list[int]) -> TreeNode:
        """
        1. Iterate on pre list and create each new node.
        2. Then save the current path to the stack.
        3. Add new node to the left if the previous node has no left child.
        4. Otherwise add right.
        5. Once we come across the same node in pre and post, we pop it
            from the stack and increase the index on post list.
        6. The above is like in the post list, when we visited post[i], all
            the child nodes rooted on post[i] has been visited previously, so
            we could use pre to create new node, then use post to check if
            all the nodes are created.
        """
        stack = [TreeNode(pre[0])]
        iPost = 0
        for iPre in range(1, len(pre)):
            currNode = TreeNode(pre[iPre])
            while stack[-1].val == post[iPost]:
                stack.pop()
                iPost += 1

            if not stack[-1].left:
                stack[-1].left = currNode
            else:
                stack[-1].right = currNode

            stack.append(currNode)

        return stack[0]
