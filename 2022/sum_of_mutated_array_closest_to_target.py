"""
https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/
"""


class Solution:
    def findBestValue(self, arr: list[int], target: int) -> int:
        """
        Simply sorte the list in reverse order, then starting checking the
        minimum number at the tail of the sorted list:

        1. If current target >= minNum * len(list), it means the minimum number
            is too small, we could get rid of it from the target by
            target - list.pop()
        2. At the end:
            2.1 If the sortedList is empty, it means we cannot reach the 
                target even with the largest number, so simply return the
                largest number instead.
            2.2 Else, it means using the remaining number in the list could
                achieve greater sum than the target. So we try to split the
                remaining target evenly on the remaining numbers avaialble
                at the remaining list.
                2.2.1 Since if there is a tie, we want to round to the small
                    integer side, thus we just try to reduce the remainTarget
                    a bit in order to make it round to the small part.
        """
        sortedList = sorted(arr, reverse=True)
        maxNum = sortedList[0]
        remainTarget = target
        while sortedList and remainTarget >= sortedList[-1] * len(sortedList):
            remainTarget -= sortedList.pop()

        if sortedList:
            return int(round((remainTarget - 0.0001) / len(sortedList)))

        return maxNum


print(Solution().findBestValue([2, 3, 5], 10))
