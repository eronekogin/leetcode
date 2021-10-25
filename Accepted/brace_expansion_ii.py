"""
https://leetcode.com/problems/brace-expansion-ii/
"""


class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        stack: list[set[str] or str] = []

        # Make sure all commas are contained by {}
        for c in '{' + expression + '}':
            if c == '{':
                stack.append(c)
            elif c == '}':
                while stack[-2] == ',':
                    s2 = stack.pop()
                    stack.pop()  # Pop comma sign.
                    stack[-1].update(s2)  # Combine s1 and s2.

                currSet = stack.pop()
                stack[-1] = currSet  # Update { with the caculated set.
            elif c == ',':
                stack.append(',')
            else:
                stack.append(set(c))

            # Handle concatenation case.
            while len(stack) > 1 and isinstance(stack[-1], set) and isinstance(stack[-2], set):
                s2 = stack.pop()
                s1 = stack.pop()
                stack.append({w1 + w2 for w1 in s1 for w2 in s2})

        return sorted(stack.pop())


print(Solution().braceExpansionII("{a,b},x{c,{d,e}y}"))
