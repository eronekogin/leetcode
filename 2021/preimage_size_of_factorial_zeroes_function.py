"""
https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/
"""


class Solution:
    def preimageSizeFZF(self, K: int) -> int:
        """
        1. The number of trailing zeros in x! is given by the minimum between
            the number of factor 2 and the number of factor 5 in x.
        2. Since there will always be more factor 2 than factor 5 in x!, the
            number of trailing zeros in x! will simply depend on the total
            number of factor 5 in x!.
        3. Suppose f(x) is the number of trailing zeros in x's factorial, then
            we have:
            3.1 Whenever x is a multiple of 5, f(x) will increase, and the
                increment is the total number of factor 5 in x. For example:
                If x in [0, 4], f(x) = 0
                If x == 5, f(x) = 0 + 1 = 1
                If x in [5, 9], f(x) = 1
                If x == 10, f(x) = 1 + 1 = 2
                ...
                If x in [20, 24], f(x) = 4
                if x == 25, f(x) = 4 + 2 = 6
                ...
            3.2 Since the increment of f(x) is not the same, some k is not
                reachable, such as k = 5.
            3.3 Suppose x = 5i and f(x) = k, then for y in [x + 1, x + 4],
                it does not contain any new factor 5 in y, so f(y) = k. Then
                for y = x + 5 = 5(i + 1), f(y) will at least be larger than k.
                In other words, for a valid k, there will be only 5 matched
                integers.
        4. Now our goal becomes to check if given K is valid or not:
            4.1 Suppose x = a0 * 5^0 + a1 * 5^1 + a2 * 5^2 + ..., where a0, a1
                , ... should be among [0, 4]. Then:
                f(x) = x / 5 + x / 5^2 + x / 5^3 + ..., this is because f(x) is
                equal to the number of factor 5 in x's factorial and in order
                to calculate that, we could count how many multiple of 5^1,
                5^2, 5^3, ... from [1, x].
            4.2 So f(x) = a1 * 1 + a2 * (1 + 5^1) + a3 * (1 + 5^1 + 5^2) + ...
            4.3 Suppose s(x) = 1 + 5 * s(x - 1), then:
                f(x) = a1 * s(0) + a2 * s(1) + a3 * s(2) + ...
            4.4 Then for any valid k, a1, a2, ... should be less than 5,
                otherwise k is not valid.
        """
        # First calculate the maximum s[i] based on the value of K.
        s = [1]
        curr = s[-1] * 5 + 1
        while curr <= K:
            s.append(curr)
            curr = s[-1] * 5 + 1

        # Then check k against each item in s.
        for si in reversed(s):
            ai, K = divmod(K, si)
            if ai == 5:  # Invalid k.
                return 0

        return 5  # k is valid.
