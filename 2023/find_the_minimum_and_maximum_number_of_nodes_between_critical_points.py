"""
https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/
"""


from test_helper import ListNode


class Solution:
    """
    Solution
    """

    def nodes_between_critical_points(self, head: ListNode) -> list[int]:
        """
        nodes_between_critical_points
        """
        curr_distance = -1
        first_point_distance = -1
        prev_point_distance = -1
        min_distance = 10 ** 6
        max_distance = 0
        prev = None
        curr = head
        while curr:
            curr_distance += 1
            if prev is not None and curr.next and (
                prev.val < curr.val > curr.next.val or
                prev.val > curr.val < curr.next.val
            ):
                if first_point_distance == -1:
                    first_point_distance = curr_distance
                else:
                    min_distance = min(
                        min_distance, curr_distance - prev_point_distance)

                    max_distance = curr_distance - first_point_distance

                prev_point_distance = curr_distance

            prev = curr
            curr = curr.next

        if max_distance == 0:  # Not enough nodes.
            return [-1, -1]

        return [min_distance, max_distance]
