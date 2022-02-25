"""
https://leetcode.com/problems/verbal-arithmetic-puzzle/
"""


class Solution:
    def isSolvable(self, words: list[str], result: str) -> bool:
        def dfs(
            charIndex: int,
            wordIndex: int,
            carry: int,
            usedDigits: set[int],
            charToDigit: dict[str, int]
        ) -> bool:
            if charIndex == maxLen:  # Reaching the last digit.
                return not carry

            if wordIndex == len(words) + 1:  # Scanned all words.
                digitSum = carry
                for w in words:
                    if charIndex < len(w):
                        digitSum += charToDigit[w[-charIndex - 1]]

                if digitSum % 10 == charToDigit[result[-charIndex - 1]]:
                    return dfs(
                        charIndex + 1,
                        0,
                        digitSum // 10,
                        usedDigits,
                        charToDigit
                    )

                return False  # Last digit is not matching on result.

            # Otherwise continue scanning the remaining words
            if (wordIndex < len(words) and charIndex >= len(words[wordIndex])):
                return dfs(
                    charIndex,
                    wordIndex + 1,
                    carry,
                    usedDigits,
                    charToDigit
                )

            currChar = allWords[wordIndex][-charIndex - 1]
            if currChar in charToDigit:  # Already in map.
                return dfs(
                    charIndex,
                    wordIndex + 1,
                    carry,
                    usedDigits,
                    charToDigit
                )

            # Build the next char to digit map.
            if currChar in leadingChars:
                start = 1
            else:
                start = 0

            for nextDigit in range(start, 10):
                if nextDigit not in usedDigits:
                    usedDigits.add(nextDigit)
                    charToDigit[currChar] = nextDigit
                    if dfs(
                        charIndex,
                        wordIndex + 1,
                        carry,
                        usedDigits,
                        charToDigit.copy()
                    ):
                        return True

                    usedDigits.remove(nextDigit)

            return False  # Not possible.

        allWords = words + [result]
        leadingChars = {w[0] for w in allWords if len(w) > 1}
        maxLen = max(len(w) for w in allWords)

        if len(result) < maxLen:  # Result is not large enough.
            return False

        return dfs(0, 0, 0, set(), dict())
