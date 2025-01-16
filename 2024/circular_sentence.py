"""
https://leetcode.com/problems/circular-sentence/description/
"""


class Solution:
    """
    Solution
    """

    def is_circular_sentence(self, sentence: str) -> bool:
        """
        is circular sentence
        """
        words = sentence.split()
        words.append(words[0])
        return all(
            words[i][-1] == words[i + 1][0]
            for i in range(len(words) - 1)
        )
