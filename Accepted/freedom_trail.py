"""
https://leetcode.com/problems/freedom-trail/
"""


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        def minDistance(start: int, end: int) -> int:
            """
            Get the minimum distance between two points on the ring.
            """
            dist = abs(end - start)
            return min(dist, n - dist)

        idxMemo = {}  # {char: indexes in the ring.}
        for i, c in enumerate(ring):
            idxMemo[c] = idxMemo.get(c, []) + [i]

        n = len(ring)

        # key is the current start positions on the ring.
        # value is the minimum steps taken to get to that position from
        # the last position.
        currState = {0: 0}
        for c in key:
            nextState = {}
            for end in idxMemo[c]:
                nextState[end] = min(
                    currState[start] + minDistance(start, end)
                    for start in currState)

            currState = nextState

        # Since pressing button will take 1 step, after we have guessed all the
        # chars in the key, it will take len(key) steps to press the button.
        return min(currState.values()) + len(key)


print(Solution().findRotateSteps('godding', 'gd'))
