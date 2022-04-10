"""
https://leetcode.com/problems/maximum-students-taking-exam/
"""


class Solution:
    def maxStudents(self, seats: list[list[str]]) -> int:
        def count_bits(num: int) -> int:
            # Count how many bits having value 1 in num.
            cnt = 0
            while num:
                cnt += 1
                num &= num - 1

            return cnt

        R, C = len(seats), len(seats[0])
        validSeats = []

        # Calculate valid seats mask for each row.
        for row in seats:
            curr = 0
            for seat in row:
                curr = (curr << 1) + (seat == '.')

            validSeats.append(curr)

        # dp[i][mask] stands for the maximum students on ith row with students
        # following the mask.
        dp = [[-1] * (1 << C) for _ in range(R + 1)]
        dp[0][0] = 0
        for r in range(1, R + 1):
            seatMask = validSeats[r - 1]
            for studentMask in range(1 << C):
                validBits = count_bits(studentMask)

                # 1. Check if a student mask is a subset of seatMask so that
                #   the target student could sit on a seat.
                # 2. The student should not sit next to each other.
                if (
                    studentMask & seatMask == studentMask and
                    studentMask & (studentMask >> 1) == 0
                ):
                    # Then check the upper student mask and make sure that
                    # 1. no student is on the upper left.
                    # 2. no student is on the upper right.
                    # Then the upper mask is a valid candidate for the current
                    # student mask.
                    for upperStudentMask in range(1 << C):
                        if (
                            studentMask & (upperStudentMask >> 1) == 0 and
                            studentMask & (upperStudentMask << 1) == 0 and
                            dp[r - 1][upperStudentMask] != -1
                        ):
                            dp[r][studentMask] = max(
                                dp[r][studentMask],
                                dp[r - 1][upperStudentMask] + validBits
                            )

        return max(dp[-1])
