"""
https://leetcode.com/problems/race-car/
"""


class Solution:
    def racecar(self, target: int) -> int:
        """
        1. The result of consectuive A instructions result the car to move to
            the position with 1 + 2 + 4 + ... + 2^n = 2^n - 1.
        2. Suppose the total bit length of target is n, then 2^(n - 1) - 1 <
            t <= 2^n - 1.
        3. If t == 2^n - 1, then we only need n consecutive A instructions to
            get to the target, which is the best choice.
        4. If t < 2^n - 1:
            4.1 Suppose dp[i] stands for the shortest steps by moving the car
                from 0 to i with initial speed 1.
            4.2 We could first move the car to position 2^n - 1, which passed
                our target, then walk back, which makes:
                    dp[i] = n + 1 + dp[2^n - 1 - t]
            4.3 We could also first move the car closer to our target, which
                is position 2^(n - 1) - 1, then turn and move back a few times,
                then turn again and move towards our target, in this case, we
                have:
                    dp[i] = (n - 1) + 1 + m + 1 + dp[
                        t - ((2^(n - 1) - 1) - (2^m - 1))]
                4.3.1 We don't know how much m we need to walk back, so here
                    we simply try every possible m from 0 to n - 1 and take
                    the minimum steps generated from that.
            4.4 Finally our dp[i] will be the minimum among 4.2 and 4.3.
        """
        def move(t: int) -> int:
            if t not in steps:
                n = t.bit_length()
                lower, higher = (1 << (n - 1)) - 1, (1 << n) - 1
                if t == higher:
                    steps[t] = n
                else:
                    # First passing the target, then walk back.
                    minSteps = move(higher - t) + n + 1

                    # Or move closest enough to the target, then walk back,
                    # move m steps, then walk back.
                    for m in range(n - 1):
                        minSteps = min(minSteps, move(
                            t - lower + ((1 << m) - 1)) + n + m + 1)

                    steps[t] = minSteps

            return steps[t]

        steps = {0: 0}  # {position: shortest steps needed}
        return move(target)
