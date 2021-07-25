"""
https://leetcode.com/problems/least-operators-to-express-number/
"""


class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        """
        1. pos[k] stands for the number of opeartors needed to get
            target % (x ^ (k + 1)), suppose r is the result,
            then we could add r times (x/x) to achieve that, the number
            of operators needed will be r * 2, this is because each
            add will need one plus operator and one divide operator.
        2. neg[k] stands for the number of operators needed to get
            x ^ (k + 1) - (target % (x ^ (k + 1))), suppose r is the
            result, then we could subtract r times (x/x) to achieve that,
            the number of opeartor will be r * 2 as each subtract need
            one subtract operator and one divide operator.
        """
        pos = neg = k = 0
        y = target
        while y:
            y, r = divmod(y, x)
            if k:
                pos, neg = min(r * k + pos, (r + 1) * k +
                               neg), min((x - r) * k + pos, (x - r - 1) * k + neg)
            else:
                pos = r << 1
                neg = (x - r) << 1

            k += 1

        return min(pos, k + neg) - 1
