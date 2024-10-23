"""
https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/
"""


class Node:
    """
    Prefix tree node
    """

    def __init__(self) -> None:
        self.cnt = 0
        self.children: dict[str, Node] = {}


class Solution:
    """
    Solution
    """

    def sum_prefix_scores(self, words: list[str]) -> list[int]:
        """
        sum prefix scores
        """

        root = Node()

        for w in words:
            curr = root
            for c in w:
                if c not in curr.children:
                    curr.children[c] = Node()

                curr.children[c].cnt += 1
                curr = curr.children[c]

        rslt: list[int] = []
        for w in words:
            curr = root
            cnt = 0
            for c in w:
                cnt += curr.children[c].cnt
                curr = curr.children[c]

            rslt.append(cnt)

        return rslt
