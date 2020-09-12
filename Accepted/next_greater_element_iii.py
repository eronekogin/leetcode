"""
https://leetcode.com/problems/next-greater-element-iii/
"""


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        """
        This is similar as finding the next lexicographical permutation which
        follows the solution as below:
            0. Suppose our number is 0 1 2 5 3 3 0.
            1. Find the longest contiguous decreasing suffix to the right side.
                This is already the largest permuation for this part of the
                digits. In our case, it is 5 3 3 0.
            2. Take the nearest digit on the left side of the head of the
                suffix as the pivot, then swap it with the smallest number
                that is greater than the pivot, in our case, pivot=2, swap=3.
            3. Now the new prefix (everthing in the original sequence except
                the suffix) is minimized, in our case prefix=0 1 3
            4. Then since suffix is still in descending order, we reverse it
                to make it the smallest number in the next permuation. In our
                case, now suffix=0 2 3 5.
            5. So our final result will be 0 1 3 0 2 3 5.
        """
        MAX_32_INT = 1 << 31 - 1
        digits = []

        # Get the digits from the current number.
        currNum = n
        while currNum:
            currNum, r = divmod(currNum, 10)
            digits.append(r)

        # Find the longest decreasing suffix.
        i, maxLen = 1, len(digits)
        while i < maxLen and digits[i] >= digits[i - 1]:
            i += 1

        if i == maxLen:  # The current permuation is already the last one.
            return -1

        # Find the smallest digit in the suffix that is greater than the pivot.
        j, pivot = 0, digits[i]
        while j < i and digits[j] <= pivot:
            j += 1

        digits[j], digits[i] = pivot, digits[j]

        # Then reverse the suffix.
        digits[:i] = digits[:i][::-1]

        # Get the number from the current digits.
        currNum = sum(num * 10 ** i for i, num in enumerate(digits))

        if currNum > MAX_32_INT:  # Greater than 32 bits integer limit.
            return -1

        return currNum
