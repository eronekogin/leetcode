"""
https://leetcode.com/problems/queue-reconstruction-by-height/
"""


from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
        Sort the input people with height in descending order and count in
        ascending order. Then for the tallest people, their positions are
        strictly determined by the count of how many people taller and equal
        than himself in front of him. Then for the second tallest people, we
        just insert them into the new array with the count as its index.

        For example:
        people=[[7,0], [7,1], [6,1], [5,0]]
        sorted_people=[[7,0], [7,1], [6, 1], [5, 0]]
        queue=[[7,0], [7,1]]
        -> queue=[[7,0], [6,1], [7,1]]
        -> queue=[[5,0], [7,0], [6,1], [7,1]]
        """
        queue = []
        for p in sorted(people, key=lambda x: (-x[0], x[1])):
            queue.insert(p[1], p)

        return queue
