"""
https://leetcode.com/problems/escape-a-large-maze/
"""


class Solution:
    def isEscapePossible(
        self,
        blocked: list[list[int]],
        source: list[int],
        target: list[int]
    ) -> bool:
        """
        1. If the total length of blocked is B, the maximum area those
            blocks could block is B * (B - 1) // 2. We could simply put
            them on the diagonal to achieve the maximum blocked area:
            0    oooox
            1    ooox
            2    oox
            3    ox
            4    x
            B = 5, blocked area is 4 + 3 + 2 + 1 + 0 = 5 * 4 / 2 = 10.
        2. Then we could do a bfs search from source cell to target. when
            we have walked more steps than the above maximum blocked area,
            we could take that we are no longer blocked if we still have
            not reached the target yet.
        3. Notice that we should check both sides: from source to target
            and from target to source to make sure both sides are not
            blocked by those blockers.
        """
        def walk(source: list[int], target: list[int]) -> bool:
            currCells = [source]
            visited = {tuple(source)}
            for r, c in currCells:
                for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if 0 <= nr < MAX_POSITION and 0 <= nc < MAX_POSITION and \
                            (nr, nc) not in visited and (nr, nc) not in blocks:
                        if [nr, nc] == target:
                            return True

                        currCells.append([nr, nc])
                        visited.add((nr, nc))

                if len(currCells) > MAX_BLOCKED_AREA:
                    return True

            return False

        if not blocked:  # No blocks.
            return True

        B = len(blocked)
        MAX_POSITION = 10 ** 6
        MAX_BLOCKED_AREA = (B * (B - 1)) >> 1
        blocks = {tuple(cell) for cell in blocked}
        return walk(source, target) and walk(target, source)


print(Solution().isEscapePossible(
    [[0, 1], [1, 0]],
    [0, 0],
    [0, 2]
))
