"""
https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/
"""


class Solution:
    def minimizeTheDifference(self, mat: list[list[int]], target: int) -> int:
        rows = [sorted(row) for row in mat]
        currSums = {0}

        for row in rows:
            nextSums = set()
            for s in currSums:
                for v in row:
                    nextSums.add(s + v)
                    if s + v >= target:
                        break
            
            currSums = nextSums
        
        return min(abs(s - target) for s in currSums)


        
print(Solution().minimizeTheDifference([[4,2,6],[2,1,8],[3,9,10],[7,8,9],[6,3,6],[5,5,10],[7,1,9],[3,1,5],[1,3,3],[3,2,8]], 61))