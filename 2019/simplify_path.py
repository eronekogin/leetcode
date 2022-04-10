"""
https://leetcode.com/problems/simplify-path/
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        currPath = []
        for item in path.split('/'):
            if item and item != '.':
                if item == '..':
                    if currPath:  # Haven't reached the root yet.
                        currPath.pop()
                else:
                    currPath.append(item)

        return '/' + '/'.join(currPath)


path = "/../"
print(Solution().simplifyPath(path))
