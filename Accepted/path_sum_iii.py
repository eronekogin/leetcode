"""
https://leetcode.com/problems/path-sum-iii/
"""


from test_helper import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        """
        | -- preSum -- |
        1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
        | ------- currSum ------ |

        1. If currSum - preSum == t, then path 4 -> 5 -> 6 is a candidate.
        2. After we have scanned all the children for node #6, we go back to
        node #5 to check other paths.
        """
        prePathSums = {0: 1}  # sum of previous paths: number of occurrences.

        def search_path(currNode: TreeNode, preSum: int, t: int) -> int:
            """
            1. Try to find all the paths which ends at the current node 
            with their summary as t.
            2. Then try to find all the paths which ends at the current node's
            left and right child with their summary as t.
            """
            if not currNode:
                return 0

            currSum = preSum + currNode.val
            paths = prePathSums.get(currSum - t, 0)
            prePathSums[currSum] = prePathSums.get(currSum, 0) + 1

            paths += search_path(currNode.left, currSum, t) + search_path(
                currNode.right, currSum, t)

            # When going to other paths that do not include the current node,
            # remove it from the prePathSums dictionary.
            prePathSums[currSum] -= 1

            return paths

        return search_path(root, 0, target)
