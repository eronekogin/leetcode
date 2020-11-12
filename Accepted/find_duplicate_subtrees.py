"""
https://leetcode.com/problems/find-duplicate-subtrees/
"""


from typing import List
from collections import defaultdict


from test_helper import TreeNode


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        """
        Serialize each subtree with a unique identification. Then check if
        such identification was seen before.
        """
        def get_uid(r: TreeNode) -> int:
            if r:
                uid = uids[(r.val, get_uid(r.left), get_uid(r.right))]
                dupTrees[uid].append(r)
                return uid

        dupTrees, uids = defaultdict(list), defaultdict

        # Set the uid to the current length of the uids is absent to make the
        # uid unique.
        uids.default_factory = uids.__len__

        get_uid(root)
        return [roots[0] for roots in dupTrees.values() if len(roots) > 1]
