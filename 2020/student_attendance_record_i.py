"""
https://leetcode.com/problems/student-attendance-record-i/
"""


class Solution:
    def checkRecord(self, s: str) -> bool:
        isAbsent, start, n = False, 0, len(s)
        while start < n:
            if s[start] == 'A':
                if isAbsent:
                    return False

                isAbsent = True
            elif s[start] == 'L':
                end = start
                while end + 1 < n and s[end + 1] == 'L':
                    end += 1

                if end - start + 1 > 2:  # Have more than 2 contiguous Lates.
                    return False

                start = end

            start += 1

        return True


print(Solution().checkRecord("PPALLL"))
