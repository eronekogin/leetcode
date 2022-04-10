"""
https://leetcode.com/problems/escape-the-ghosts/
"""


class Solution:
    def escapeGhosts(self, ghosts: list[list[int]], target: list[int]) -> bool:
        """
        1. Suppose player is walking from A to C while in the middle of AC it
            will come across a ghost who is walking from B to D. Then AD = BD.
            So AC = AD + DC = BD + DC > BC. So the ghost could just go
            directly to the target point and arrives earlier than the player.
            So for any ghost, the optimized route should be heading directly
            towards the target point and wait the player there.
        2. The total distance from the start point to the target point is
            abs(x1 - x2) + abs(y1 - y2).
        """
        tr, tc = target
        d = abs(tr) + abs(tc)
        return all(d < abs(gr - tr) + abs(gc - tc) for gr, gc in ghosts)


print(Solution().escapeGhosts([[2, 0]], [1, 0]))
