"""
https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/description/
"""


from collections import defaultdict, deque


class Solution:
    """
    Solution
    """

    def maximum_invitations(self, favorite: list[int]) -> int:
        """
        maximum_invitations
        """
        def find_distance(a: int, b: int):
            max_distance = 0
            queue = deque()
            for child in children[a]:
                if child != b:
                    queue.append([child, 1])

            while queue:
                curr, distance = queue.popleft()
                max_distance = max(max_distance, distance)
                queue.extend(
                    [next_node, distance + 1]
                    for next_node in children[curr]
                )

            return max_distance

        # Find the largest circle.
        n = len(favorite)
        max_circle_len = 0
        visited = [0] * n

        for i in range(n):
            if not visited[i]:
                start = curr = i
                curr_visited = set()

                while not visited[curr]:
                    visited[curr] = 1
                    curr_visited.add(curr)
                    curr = favorite[curr]  # Go to the next person.

                if curr in curr_visited:  # Found a new circle.
                    curr_circle_len = len(curr_visited)
                    while start != curr:
                        curr_circle_len -= 1
                        start = favorite[start]

                    max_circle_len = max(max_circle_len, curr_circle_len)

        # Find mutual pairs contains only two nodes.
        pairs = []
        visited = [0] * n
        children = defaultdict(list)
        for i, j in enumerate(favorite):
            children[j].append(i)

            if favorite[j] == i and not visited[i]:
                pairs.append([i, j])
                visited[i] = 1
                visited[j] = 1

        # For each pair, find the longest distance from their own sides.
        rslt = 0

        for a, b in pairs:
            da = find_distance(a, b)
            db = find_distance(b, a)
            rslt += 2 + da + db  # 2 stands for a, b themselves.

        return max(rslt, max_circle_len)


print(Solution().maximum_invitations([2, 2, 1, 2]))
