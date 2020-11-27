"""
https://leetcode.com/problems/bulb-switcher-ii/
"""


from typing import List


class Solution:
    def flipLights(self, n: int, m: int) -> int:
        """
        1. With the definition of the 4 actions, the state of the i+6th index
            is the same as the ith state, which means the first 6 indexes
            determine the unique state of all the bulbs.
        2. Then for each kind of action A, B, AB = BA. Also for any kind of
            action A, AA = restore to the previous state. So in the end we only
            need to care whether each kind of action is performed zero or one
            time.
        3. Suppose we perform all the four actions a, b, c, d, then the
            states of the first 6 bulbs are:
            s1 = 1 + a + c + d
            s2 = 1 + a + b
            s3 = 1 + a + c
            s4 = 1 + a + b + d
            s5 = 1 + a + c = s3
            s6 = 1 + a + b = s2
            (s1 + s2 + s3) % 2 = (3 + 3a + b + 2c + d) % 2 = 1 + a + b + d = s4

            So the first three bulbs could determine the unique states.
        """
        stateLen = min(n, 3)
        if m == 0:  # No step is performed.
            return 1

        if m == 1:  # 1 step is performed.
            # Case 1 bulb: 1, 0.
            # Case 2 bulbs: 10, 01, 00.
            # Case 3 bulbs: 101, 010, 000, 011.
            return [2, 3, 4][stateLen - 1]

        if m == 2:  # 2 steps are performed.
            # Case 1 bulb: 1, 0.
            # Case 2 bulbs: 10, 01, 00, 11.
            # Case 3 bulbs: 111, 000, 010, 101, 110, 001, 011.
            return [2, 4, 7][stateLen - 1]

        # If more steps are performed.
        return [2, 4, 8][stateLen - 1]
