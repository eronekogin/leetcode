"""
https://leetcode.com/problems/minimum-space-wasted-from-packaging/
"""


from bisect import bisect_right


class Solution:
    def minWastedSpace(self, packages: list[int], boxes: list[list[int]]) -> int:
        sortedPackages = sorted(packages)
        minTotalBoxSpaces = -1
        for boxSizes in boxes:
            boxSizes.sort()
            if sortedPackages[-1] > boxSizes[-1]:
                continue
            
            totalBoxSpaces = 0
            currUsedBoxes = 0
            for size in boxSizes:
                coveredPackages = bisect_right(sortedPackages, size, currUsedBoxes)
                totalBoxSpaces += (coveredPackages - currUsedBoxes) * size
                currUsedBoxes = coveredPackages
            
            if minTotalBoxSpaces == -1:
                minTotalBoxSpaces = totalBoxSpaces
            else:
                minTotalBoxSpaces = min(minTotalBoxSpaces, totalBoxSpaces)
        
        if minTotalBoxSpaces == -1:
            return -1
        
        return (minTotalBoxSpaces - sum(packages)) % (10 ** 9 + 7)



