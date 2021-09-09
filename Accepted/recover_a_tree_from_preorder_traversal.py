"""
https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/
"""


from test_helper import TreeNode


class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        currLevel = 0
        stack = []
        end, N = 0, len(traversal)
        while end < N:
            if traversal[end] == '-':
                currLevel += 1
                end += 1
            else:  # Found a number.
                start = end
                while end < N and traversal[end].isdigit():
                    end += 1

                newNode = TreeNode(int(traversal[start: end]))
                if stack:
                    if currLevel > stack[-1][0]:
                        stack[-1][1].left = newNode
                    else:
                        while stack[-1][0] >= currLevel:
                            stack.pop()

                        stack[-1][1].right = newNode

                stack.append((currLevel, newNode))
                currLevel = 0  # Reset currLevel.

        return stack[0][1]


print(Solution().recoverFromPreorder("1-401--349---90--88").print_tree())
