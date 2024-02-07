"""
https://leetcode.com/problems/earliest-possible-day-of-full-bloom/description/
"""


class Solution:
    """
    Solution
    """

    def earliest_full_bloom(self, plant_time: list[int], grow_time: list[int]) -> int:
        """
        Basically, the logic is that the grow time is strictly continuous
        whereas the plant time is more flexible. So we want to make sure
        that there is something going on (plant and grow of other flowers)
        when a flower is growing.

        With that said, we sort all flowers by grow time in ascending order
        because as we move along the flowers, the minimum leading time is
        monotonically increasing so we have better chance to do more jobs
        during the time of growth of slow-growing flowers.
        """
        full_bloom_time = 0
        for grow, plant in sorted(zip(grow_time, plant_time)):
            full_bloom_time = max(full_bloom_time, grow) + plant

        return full_bloom_time
