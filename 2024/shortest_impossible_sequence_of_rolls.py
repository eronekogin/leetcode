"""
https://leetcode.com/problems/shortest-impossible-sequence-of-rolls/description/
"""


class Solution:
    """
    Solution
    """

    def shortest_sequence(self, rolls: list[int], k: int) -> int:
        """
        Check the first occurrence of all numbers from 1 to k starting
        from rolls[0], suppose rolls[i] is the rightmost occurrence, then
        from rolls[0] to rolls[i] we form a complete set.

        Continue to check such complete set until no more can be found.

        Suppose the number of complete sets are x, then x + 1 is the
        shortest sequence to create so that such sequence does not exist in rolls.

        We can simply form such sequence by taking the last number from each
        complete set, then taking a number that does not exist in the 
        last part of the rolls for form a x + 1 length sequence that
        cannot be formed from rolls.
        """
        min_len = 1
        s = set()

        for x in rolls:
            s.add(x)
            if len(s) == k:
                min_len += 1
                s.clear()

        return min_len
