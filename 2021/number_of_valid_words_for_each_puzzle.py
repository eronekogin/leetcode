"""
https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/
"""


from collections import Counter


class Solution:
    def findNumOfValidWords(
        self,
        words: list[str],
        puzzles: list[str]
    ) -> list[int]:
        def bit_mask(word: str) -> int:
            mask = 0
            for c in word:
                mask |= 1 << (ord(c) - BASE)

            return mask

        BASE = ord('a')

        # Build bit mask for each word.
        masks = Counter(map(bit_mask, words))

        # Calculate answers.
        answers = []
        for puzzle in puzzles:
            firstCharMask = 1 << (ord(puzzle[0]) - BASE)
            cnt = masks[firstCharMask]  # Match first char only.

            # Initialize submask with remaining chars of the puzzle.
            subMask = currMask = bit_mask(puzzle[1:])

            # Then check each possible submask and count the number of
            # matching words.
            while subMask:
                cnt += masks[firstCharMask | subMask]

                # Make sure the next submask is a subset of the previous
                # submask
                subMask = (subMask - 1) & currMask

            answers.append(cnt)

        return answers
