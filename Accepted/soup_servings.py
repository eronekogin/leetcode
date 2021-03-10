"""
https://leetcode.com/problems/soup-servings/
"""


class Solution:
    def soupServings(self, N: int) -> float:
        """
        1. Take one time serve as 25 ml from both A and B.
        2. Then suppose f(a, b) stands for how many serve times are left in
            A and B
        3. Then the four options become f(a - 4, b), f(a - 3, b - 1),
            f(a - 2, b - 2), f(a - 1, b - 3).
        4. Notice that we don't have the option to use all B at one time, so
            when N becomes larger, it is more difficult to make B empty first.
        5. When N is greater than 4800, the result will be very closer to 1.
        """
        def serve(a: float, b: float) -> float:
            if (a, b) not in memo:
                if a <= 0 and b <= 0:  # Both empty.
                    return 0.5  # Only need half of the probability.
                elif a <= 0:  # A is empty first.
                    return 1
                elif b <= 0:  # B is empty first.
                    return 0

                memo[(a, b)] = 0.25 * (
                    serve(a - 4, b) + serve(a - 3, b - 1) +
                    serve(a - 2, b - 2) + serve(a - 1, b - 3))

            return memo[(a, b)]

        if N >= 4800:
            # When N is larger enough, the probability is closer to 1.
            return 1

        memo = {}
        times = N / 25
        return serve(times, times)
