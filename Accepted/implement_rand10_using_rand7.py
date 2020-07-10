from random import randint


def rand7(self) -> int:
    return randint(1, 7)


class Solution:
    def rand10_1(self) -> int:
        """
        Use rejection sampling to generate rand49 from rand7 with the matrix
        showed as below:

            1  2  3  4  5  6  7
        1   1  2  3  4  5  6  7
        2   8  9  10 11 12 13 14
        3   15 16 17 18 19 20 21
        4   22 23 24 25 26 27 28
        5   29 30 31 32 33 34 35
        6   36 37 38 39 40 41 42
        7   43 44 45 46 47 48 49

        So 7 * (r - 1) + c will give us 1 to 49 when r and c in [1, 7].

        Now our valid range result a falls in 1 to 40, so that a - 1 gives us
        0 to 39 and (a - 1) % 10 gives us 0 to 9. In the end, (a - 1) % 10 + 1
        gives us 1 to 10.

        The probability that i falls in [1, 40] is calculated as follows:
        p(i) = 1/49 + 9/49 * (1/49) + (9/49)^2 * (1/49) + ...
            = (1/49) * (1 + 9/49 + (9/49)^2 + (9/49)^3 + ...)
            = (1/49) * (1 / (1 - 9/49))  # Limit for a Proportional Sequence.
            = 1/49 * 49/40 = 1/40.

        That's why it will generate rand40. 
        """
        i = 41
        while i > 40:
            i = 7 * (rand7() - 1) + rand7

        return 1 + (i - 1) % 10

    def rand10_2(self) -> int:
        """
        By taking the advantage of the numbers that falls out of the target
        range, we could think like this:
        1. For numbers in [41, 49] gives us [1, 9], after invoking another
            rand7() we will get rand63, which will give us rand60.
        2. For numbers in [61, 63] gives us [1, 3], after invoking another
            rand7() we will get rand21, which will give us rand20.
        3. If our number unfortunately falls to 21, then we start again.
        """
        def generate(a: int, t: int) -> int:
            i = 7 * (a - 1) + rand7()
            if i <= t:
                return 1 + (i - 1) % 10

            return 0  # The number falls out of range.

        while True:
            i = generate(rand7(), 40)
            if not i:
                i = generate(i - 40, 60)

            if not i:
                i = generate(i - 60, 20)

            if i:
                return i
