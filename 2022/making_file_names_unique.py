"""
https://leetcode.com/problems/making-file-names-unique/
"""


class Solution:
    def getFolderNames(self, names: list[str]) -> list[str]:
        visited: dict[str, int] = {}
        for name in names:
            actualName = name
            if name in visited:
                seq = visited[name]
                while actualName in visited:
                    seq += 1
                    actualName = f'{name}({seq})'

                visited[name] = seq

            visited[actualName] = 0

        return visited.keys()
