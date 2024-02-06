"""
https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/description/
"""


class Solution:
    """
    Solution
    """

    def word_count(self, start_words: list[str], target_words: list[str]) -> int:
        """
        word_count
        """
        visited_masks: set[int] = set()
        offset = ord('a')
        for w in start_words:
            mask = 0
            for c in w:
                mask ^= 1 << (ord(c) - offset)

            visited_masks.add(mask)

        cnt = 0
        for w in target_words:
            mask = 0
            for c in w:
                mask ^= 1 << (ord(c) - offset)

            for c in w:  # remove each char and see if mask is visited before.
                if mask ^ (1 << (ord(c) - offset)) in visited_masks:
                    cnt += 1
                    break

        return cnt


print(Solution().word_count(["ant", "act", "tack"], ["tack", "act", "acti"]))
