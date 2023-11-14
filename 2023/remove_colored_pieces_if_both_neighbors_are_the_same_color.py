"""
https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/
"""


class Solution:
    """
    Solution
    """

    def winner_of_game(self, colors: str) -> bool:
        """
        winner_of_game
        """
        a = b = 0
        for i in range(1, len(colors) - 1):
            if colors[i - 1] == colors[i] == colors[i + 1]:
                if colors[i] == 'A':
                    a += 1
                else:
                    b += 1

        return a > b


print(Solution().winner_of_game('AAABABB'))
