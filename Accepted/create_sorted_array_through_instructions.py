"""
https://leetcode.com/problems/create-sorted-array-through-instructions/
https://www.topcoder.com/community/competitive-programming/tutorials/binary-indexed-trees/
"""


from typing import List


class BSTNode:

    def __init__(self, val: int):
        self.val = val
        self.left = self.right = None
        self.sameCnt = self.lessCnt = self.greaterCnt = 0


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        """
        Use binary search tree.
        """
        def build_tree_skeleton(start: int, end: int) -> BSTNode:
            if start > end:
                return

            if start == end:
                return BSTNode(nodes[start])

            m = start + ((end - start) >> 1)
            currNode = BSTNode(nodes[m])
            currNode.left = build_tree_skeleton(start, m - 1)
            currNode.right = build_tree_skeleton(m + 1, end)
            return currNode

        def add_and_count(currNode: BSTNode) -> List[int]:
            if val > currNode.val:
                currNode.greaterCnt += 1
                rslt = add_and_count(currNode.right)
                rslt[0] += currNode.lessCnt + currNode.sameCnt
            elif val < currNode.val:
                currNode.lessCnt += 1
                rslt = add_and_count(currNode.left)
                rslt[1] += currNode.greaterCnt + currNode.sameCnt
            else:
                currNode.sameCnt += 1
                rslt = [currNode.lessCnt, currNode.greaterCnt]

            return rslt

        nodes = sorted(list(set(instructions)))
        root = build_tree_skeleton(0, len(nodes) - 1)
        cost, MOD = 0, 10 ** 9 + 7
        for val in instructions:
            cost += min(add_and_count(root)) % MOD

        return cost % MOD

    def createSortedArray2(self, instructions: List[int]) -> int:
        """
        Use binary indexed tree.  x & -x could get the least significant bit.
        """
        def update(val: int):
            # Update the frequencies in the tree.
            currVal = val
            while (currVal <= M):
                tree[currVal] += 1
                currVal += currVal & -currVal

        def get(val: int):
            rslt, currVal = 0, val
            while (currVal > 0):
                rslt += tree[currVal]
                currVal -= currVal & -currVal

            return rslt

        M = max(instructions)
        tree = [0] * (M + 1)
        rslt, MOD = 0, 10**9 + 7
        for i, val in enumerate(instructions):
            # get(val - 1) could get us the total numbers that are less than
            # val in the current list. Also here i stands for how many numbers
            # that are already in the sorted list, so i - get(val) get us the
            # total numbers that are greater than val.
            rslt += min(get(val - 1), i - get(val)) % MOD
            update(val)

        return rslt % MOD


print(Solution().createSortedArray2([1, 5, 6, 2]))
