"""
https://leetcode.com/problems/chalkboard-xor-game/
"""


class Solution:
    def xorGame(self, nums: list[int]) -> bool:
        """
        1. If the total xor of nums is 0, alice already wins.
        2. if the total xor is not zero, it means at least there are 2
            different number in nums:
            2.1 If the total length of nums is even, it means the total
                number of different numbers should be odd. Then alice could
                always erase one of the different number that is not paired
                already. For example, [1, 1, 2, 3]: alice could always erase
                2 first, and when the next time alice could pick, she either
                face [1, 3] or [1, 1], and she will win in either cases.
            2.2 If the total length of nums is odd, then alice must lose as
                after she makes her move, bob will face the case when the
                total length of nums is even, and according to 2.1, bob must
                win. 
        """
        initialXor = 0
        for num in nums:
            initialXor ^= num

        return not initialXor or not (len(nums) & 1)
