"""
https://leetcode.com/problems/smallest-rotation-with-highest-score/
"""


class Solution:
    def bestRotation(self, A: list[int]) -> int:
        """
        1. Suppose the numbers in A are in (0, N - 1):
            1.1 Suppose A[i] = j, then in order to move A[i] to index j we
                needs to move k = (i + N - j) % N steps. This is the turning
                point for element A[i]: if we move 1 more step, the total
                score of A will be reduced by 1.
            1.2 Suppose we have a changes[i] which tracks the total changes
                on the total score of A at step i, then for the case in 1.1, 
                we have changes[k + 1] -= 1.
            1.3 Then for each number in A, we found its turning point k and
                reduce the changes[k + 1] by 1.
            1.4 On the other hand, for each move step, it will shift a number
                from index 0 to index N - 1, which will always add 1 to the
                total score of A, so the changes list could be initialized
                with [1] * N.
            1.5 Now we could collect the total changes for each step k, which
                is total[i] = total[i - 1] + changes[i], we could continue
                using changes list as the place to store our total changes
                for each step, where changes[i] += changes[i - 1].
            1.6 Then we could find the maximum value from the changes and then
                find the lowest index with that maximum value. This index value
                is the minimum k we need to move in order to get the highest
                score.
        2. Now for case when A[i] = 0 or N:
            2.1 Suppose A[2] = 0, then we need k = 2 steps to move A[2] to zero.
                Then the logic in 1.2 will make changes[3] -= 1.
            2.2 This looks invalid because for any A[i] = 0, moving its
                position will never change the total score.
            2.3 But remember we have initialized all the element in changes to
                1 based on the logic in 1.4, in other words, we always think
                moving 1 step will add 1 to the total score, even for A[i] = 0.
                So this adding logic couters effect in 2.1. And in the end
                A[i] = 0 will make no change to the total score of A.
            2.4 For A[i] = N, it is the same as A[i] = 0, which make no change
                to the total score of A during shifting.
        """
        N = len(A)
        changes = [1] * N
        for i in range(N):
            changes[(i - A[i] + 1) % N] -= 1

        for i in range(1, N):
            changes[i] += changes[i - 1]

        return changes.index(max(changes))
