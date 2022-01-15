"""
https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/
"""


class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        def is_sub_folder(parent: str, child: str) -> bool:
            return all(
                p == c for p, c in zip(parent.split('/'), child.split('/')))

        rslt = []
        for folderPath in sorted(folder):
            if not rslt:
                rslt.append(folderPath)
                continue

            if is_sub_folder(rslt[-1], folderPath):
                continue

            rslt.append(folderPath)

        return rslt
