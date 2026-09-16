"""
https://leetcode.com/problems/construct-string-with-minimum-cost/description/

See https://leetcode.com/problems/construct-string-with-minimum-cost/solutions/5467823/python3-aho-corasick-bottom-up-dp-by-alb-ikem/
for more details
"""


from collections import defaultdict, deque
from math import inf


class TrieNode():
    """
    Trie Node
    """

    def __init__(self):
        self.suffix_link = None
        self.output = defaultdict(lambda: 10e5)
        self.children = {}
        self.id = -1


class AhoCorasick:
    """
    Aho Corasick
    """

    def __init__(self, words, costs):
        self.init_words(words, costs)

    def init_words(self, words, costs):
        """
        init words
        """
        self.root = TrieNode()

        for i, word in enumerate(words):
            root = self.root
            for c in word:
                if c not in root.children:
                    root.children[c] = TrieNode()

                root = root.children[c]

            if root.id == -1 or costs[i] < costs[root.id]:
                root.id = i

            root.output[len(word)] = min(root.output[len(word)], costs[i])

        self.build_automata()

    def build_automata(self):
        """
        build automata
        """
        q = deque([])

        for c, node in self.root.children.items():
            q.append(node)
            node.suffix_link = self.root

        while q:
            curr = q.popleft()

            for c, node in curr.children.items():
                ptr = curr.suffix_link
                while ptr and c not in ptr.children:
                    ptr = ptr.suffix_link

                if ptr and c in ptr.children:
                    node.suffix_link = ptr.children[c]
                else:
                    node.suffix_link = self.root

                if node.suffix_link.id >= 0:
                    node.id = node.suffix_link.id

                if node.suffix_link is not self.root:
                    for length, cost in node.suffix_link.output.items():
                        node.output[length] = min(node.output[length], cost)

                q.append(node)

    def suffixes_after_appending(self, node, letter):
        """
        suffixes after appending
        """
        while node != self.root and letter not in node.children:
            node = node.suffix_link

        if letter in node.children:
            node = node.children[letter]
        else:
            node = self.root

        return node


class Solution:
    """
    Solution
    """

    def minimum_cost(self, target: str, words: list[str], costs: list[int]) -> int:
        """
        minimum cost
        """
        trie = AhoCorasick(words, costs)
        n = len(target)
        dp = [inf] * (n + 1)
        dp[0] = 0
        cur = trie.root

        for i in range(1, n + 1):
            cur = trie.suffixes_after_appending(cur, target[i - 1])

            for length, cost in cur.output.items():
                dp[i] = min(dp[i], dp[i - length] + cost)

        return int(-1 if dp[n] == inf else dp[n])
