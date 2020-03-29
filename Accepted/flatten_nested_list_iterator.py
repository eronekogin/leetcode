"""
https://leetcode.com/problems/flatten-nested-list-iterator/
"""


from typing import List


class NestedInteger:
    def __init__(self, num: int, nestedList: List['NestedInteger'] = None):
        self.num = num
        self.nestedList = nestedList

    def isInteger(self) -> bool:
        return self.nestedList is None

    def getInteger(self) -> int:
        return self.num

    def getList(self) -> List['NestedInteger']:
        return self.nestedList


class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        self.stack = [[nestedList, 0]]

    def next(self) -> int:
        # Explicitly call the hasNext method in case it is not called
        # before calling next.
        if self.hasNext():
            currItems, currIdx = self.stack[-1]
            self.stack[-1][1] += 1  # Move forward the current index.
            return currItems[currIdx].getInteger()

    def hasNext(self) -> bool:
        s = self.stack
        while s:
            currItems, currIdx = s[-1]
            if currIdx == len(currItems):  # Completed searching this list.
                s.pop()
            else:
                currItem = currItems[currIdx]
                if currItem.isInteger():
                    return True

                # Move forward the current index and
                # add the next list to stack.
                s[-1][1] += 1
                s.append([currItem.getList(), 0])

        return False  # No more item.


# [1, [2, [3], 4], [5, 6]].
n1 = NestedInteger(1)
n2 = NestedInteger(2)
n3 = NestedInteger(3)
n4 = NestedInteger(4)
n5 = NestedInteger(5)
n6 = NestedInteger(6)
n7 = NestedInteger(None, [n5, n6])
n8 = NestedInteger(None, [n3])
n9 = NestedInteger(None, [n2, n8, n4])
n0 = [n1, n9, n7]
ni = NestedIterator(n0)
while ni.hasNext():
    print(ni.next())
