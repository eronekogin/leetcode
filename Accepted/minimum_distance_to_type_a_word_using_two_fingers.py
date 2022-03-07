"""
https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/
"""


from string import ascii_uppercase


class Solution:
    def minimumDistance2(self, word: str) -> int:
        def distance(c1: str, c2: str) -> int:
            x1, y1 = divmod(ord(c1) - OFFSET, TOTAL_COLUMNS)
            x2, y2 = divmod(ord(c2) - OFFSET, TOTAL_COLUMNS)
            return abs(y2 - y1) + abs(x2 - x1)

        TOTAL_COLUMNS, OFFSET = 6, ord('A')
        TOTAL_CHARS = 26
        maxSavedDistanceByTheOtherHand = [0] * TOTAL_CHARS
        maxSavedDistance = 0
        totalDistanceByOneHand = 0

        for currChar, nextChar in zip(word, word[1:]):
            currIndex = ord(currChar) - OFFSET
            distanceUsingSameHand = distance(currChar, nextChar)
            totalDistanceByOneHand += distanceUsingSameHand

            # Put the other finger on all the chars to find the maximum
            # saving distance.
            for middle in range(TOTAL_CHARS):
                savedDistance = (
                    maxSavedDistanceByTheOtherHand[middle] +
                    distanceUsingSameHand -
                    distance(ascii_uppercase[middle], nextChar)
                )
                maxSavedDistanceByTheOtherHand[currIndex] = max(
                    maxSavedDistanceByTheOtherHand[currIndex],
                    savedDistance
                )

            maxSavedDistance = max(
                maxSavedDistance,
                maxSavedDistanceByTheOtherHand[currIndex]
            )

        return totalDistanceByOneHand - maxSavedDistance
