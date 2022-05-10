"""
https://leetcode.com/problems/find-all-good-strings/
"""


from functools import lru_cache


class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        @lru_cache(None)
        def dfs(
            currIdx: int,
            maxMatchedIdx=0,
            isLeftBound=True,
            isRightBound=True
        ) -> int:
            if maxMatchedIdx == len(evil):  # Found evil string.
                return 0

            if currIdx == n:  # Reaching end, found good string.
                return 1

            l = s1[currIdx] if isLeftBound else 'a'
            r = s2[currIdx] if isRightBound else 'z'
            candidates = [chr(i) for i in range(ord(l), ord(r) + 1)]
            cnt = 0

            # Scan all candidates against kmp list.
            for i, c in enumerate(candidates):
                nextMatchedIdx = maxMatchedIdx
                while evil[nextMatchedIdx] != c and nextMatchedIdx:
                    nextMatchedIdx = kmp[nextMatchedIdx - 1]

                cnt += dfs(
                    currIdx + 1,
                    nextMatchedIdx + (c == evil[nextMatchedIdx]),
                    isLeftBound and i == 0,
                    isRightBound and i == len(candidates) - 1
                )

            return cnt

        # Build kmp list.
        kmp: list[int] = [0]
        i, target = 1, 0
        while i < len(evil):
            if evil[i] == evil[target]:  # Forward to the next state.
                target += 1
                kmp.append(target)
                i += 1
            elif target > 0:  # Back to where the previous state will point to.
                target = kmp[target - 1]
            else:  # Back to the start point.
                kmp.append(0)
                i += 1

        return dfs(0) % (10 ** 9 + 7)
