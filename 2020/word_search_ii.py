"""
https://leetcode.com/problems/word-search-ii/
"""


from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build trie from the input words.
        root = {}
        for w in words:
            node = root
            for c in w:
                node = node.setdefault(c, {})

            # Stored the whole word to the current level.
            node[''] = w

        # Build new board formed by r + cj: value.
        chkBoard = {
            r + 1j * c: v
            for r, row in enumerate(board)
            for c, v in enumerate(row)
        }

        found = []

        def search(node, z):
            # Use dfs to search the input node and its four neighbours.
            if '' in node:
                # Pop the word out to prevent it
                # to be found again in another path.
                found.append(node.pop(''))

            c = chkBoard.get(z)
            if c in node:
                chkBoard[z] = '#'  # Marked the current item as used.
                for k in range(4):
                    # (1, 0), (0, 1), (-1, 0), (0, -1)
                    search(node[c], z + 1j ** k)

                chkBoard[z] = c  # Clear mark.

        for z in chkBoard:
            search(root, z)

        return found
