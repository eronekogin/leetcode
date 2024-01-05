"""
https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/
"""

from collections import deque, defaultdict

from test_helper import TreeNode


class Solution:
    """
    Solution
    """

    def get_directions(self, root: TreeNode, start_value: int, dest_value: int) -> str:
        """
        get_directions
        """
        graph: defaultdict[int, list[tuple[int, str]]] = defaultdict(list)
        queue = deque([root])

        # Generate graph.
        while queue:
            node = queue.popleft()
            if node.left:
                graph[node.left.val].append((node.val, 'U'))
                graph[node.val].append((node.left.val, 'L'))
                queue.append(node.left)

            if node.right:
                graph[node.right.val].append((node.val, 'U'))
                graph[node.val].append((node.right.val, 'R'))
                queue.append(node.right)

        # bfs.
        queue2: deque[tuple[int, str]] = deque([(start_value, '')])
        visited = {start_value}
        while queue2:
            curr_val, curr_path = queue2.popleft()
            if curr_val == dest_value:
                return curr_path

            for next_val, next_path in graph[curr_val]:
                if next_val not in visited:
                    visited.add(next_val)
                    queue2.append((next_val, curr_path + next_path))

        return ''
