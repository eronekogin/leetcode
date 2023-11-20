"""
https://leetcode.com/problems/number-of-valid-words-in-a-sentence/
"""


class Solution:
    """
    Solution
    """

    def count_valid_words(self, sentence: str) -> int:
        """
        count_valid_words
        """
        def is_valid_sentence(w: str):
            if w.count('-') > 1:
                return False

            n = len(w) - 1
            for i, c in enumerate(w):
                if c in '.!,' and i != n:
                    return False

                if c.isnumeric():
                    return False

                if c == '-' and (
                    i == 0 or
                    i == n or
                    not w[i - 1].isalpha() or
                    not w[i + 1].isalpha()
                ):
                    return False

            return True

        return sum(is_valid_sentence(w) for w in sentence.split())


print(Solution().count_valid_words("cat and  dog"))
