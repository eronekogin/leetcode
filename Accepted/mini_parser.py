"""
https://leetcode.com/problems/mini-parser/
"""


from test_helper import NestedInteger


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if '[' not in s:  # s contains only 1 integer.
            return NestedInteger(int(s))

        stack = []  # Stack which contains nestedInteger instances.
        currSum, sign = None, 1
        for c in s:
            if c == '[':  # Create a new instance.
                newItem = NestedInteger()
                if stack:
                    stack[-1].add(newItem)

                stack.append(newItem)
            elif c == '-':  # Minus sign found.
                sign = -1
            elif c == ',':  # Create a new instance and add it to the parent.
                if currSum is not None:  # Check for the '],' case.
                    stack[-1].add(NestedInteger(sign * currSum))
                    currSum, sign = None, 1
            elif c == ']':
                if currSum is not None:  # Check for the ']]' case.
                    stack[-1].add(NestedInteger(sign * currSum))
                    currSum, sign = None, 1

                rslt = stack.pop()  # Pop the current parent.
            else:  # Integer found.
                if currSum is None:
                    currSum = int(c)
                else:
                    currSum = currSum * 10 + int(c)

        return rslt


print(Solution().deserialize(
    '[123,[-456,[789],101],[102,-103],-104]'
))
