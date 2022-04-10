"""
https://leetcode.com/problems/design-skiplist/
"""

from random import choice


class Node:

    def __init__(self, val: int or None) -> None:
        self.val = val
        self.next: 'Node' = None
        self.down: 'Node' = None


class Skiplist:

    def __init__(self):
        self.nodes: list[Node] = [Node(None)]

    def search(self, target: int) -> bool:
        currNode = self.nodes[-1]
        while currNode:
            # Search on the same level first.
            while currNode.next and currNode.next.val <= target:
                if currNode.next.val == target:
                    return True  # Found

                currNode = currNode.next

            currNode = currNode.down  # Move to the lower level.

        return False

    def add(self, num: int) -> None:
        # Randomly determine the maximum level the new number should be
        # added to.
        maxLevel = 1
        while choice([0, 1]) == 1 and maxLevel < len(self.nodes):
            maxLevel += 1

        # If the new number needs to be inserted at the next level of the
        # current highest level.
        if maxLevel == len(self.nodes):
            newNode = Node(None)
            newNode.down = self.nodes[-1]
            self.nodes.append(newNode)

        # Now add the target number to target levels.
        currNode = self.nodes[-1]
        parent: Node = None
        currLevel = len(self.nodes)

        while currNode:
            while currNode.next and currNode.next.val <= num:
                currNode = currNode.next

            if currLevel <= maxLevel:
                # Add the new number.
                newNode = Node(num)
                newNode.next = currNode.next
                currNode.next = newNode

                # Update the down link as well.
                if parent:
                    parent.down = newNode

                parent = newNode

            currNode = currNode.down
            currLevel -= 1

    def erase(self, num: int) -> bool:
        rslt = False
        currNode = self.nodes[-1]
        while currNode:
            while currNode.next and currNode.next.val <= num:
                if currNode.next.val == num:
                    rslt = True  # Found.
                    currNode.next = currNode.next.next  # Delete node.
                    break
                else:
                    currNode = currNode.next

            currNode = currNode.down

        # Clean up dummy nodes if more than one level.
        while len(self.nodes) >= 2:
            candidate = self.nodes[-2]
            if candidate.next is None:
                self.nodes.pop()
            else:
                break

        return rslt
