"""
https://leetcode.com/problems/operations-on-tree/
"""


from collections import deque


class LockingTree:

    def __init__(self, parent: list[int]):
        self.nodes: list[list[int]] = [[p, -1] for p in parent]

        # Build nearest descendants.
        self.descendants: list[list[int]] = [[] for _ in range(len(parent))]
        for i, p in enumerate(parent):
            if p != -1:
                self.descendants[p].append(i)
    
    def _has_no_locked_ancestors(self, num: int) -> bool:
        parent = self.nodes[num][0]
        while parent != -1:
            if self.nodes[parent][1] != -1:  # Found a locked ancestor.
                return False
            
            parent = self.nodes[parent][0]
        
        return True  # Reaching the root node.

    def _check_and_unlock_descendants(self, num: int) -> bool:
        descendants = deque(self.descendants[num])
        hasLockedDescendant = False
        while descendants:
            node = descendants.popleft()
            if self.nodes[node][1] != -1:
                hasLockedDescendant = True
                self.nodes[node][1] = -1  # Unlock the descendant.
            
            descendants.extend(self.descendants[node])  # Check remaining descendants.
        
        return hasLockedDescendant
        

    def lock(self, num: int, user: int) -> bool:
        if self.nodes[num][1] != -1:  # Node is already locked.
            return False
        
        self.nodes[num][1] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.nodes[num][1] != user:  # Node is not locked by this user.
            return False
        
        self.nodes[num][1] = -1
        return True

    def upgrade(self, num: int, user: int) -> bool:
        if self.nodes[num][1] != -1:  # The current node is locked.
            return False

        if not self._has_no_locked_ancestors(num):
            return False

        if not self._check_and_unlock_descendants(num):
            return False
        
        # Lock the current node.
        self.nodes[num][1] = user
        return True
        

lockingTree = LockingTree([-1,0,3,1,0])
lockingTree.upgrade(4, 5)

