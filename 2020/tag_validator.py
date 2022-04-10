"""
https://leetcode.com/problems/tag-validator/
"""


import re


class Solution:
    def isValid(self, code: str) -> bool:
        if not code:  # The input code is empty.
            return False

        P_CDATA = re.compile(r"""
        <!\[CDATA\[  # Initial string
        .*?          # Match the smallest strings until finding the nearest ]]
        \]\]>        # The closing ]]>
        |            # Or
        t            # Match any small letter t
        """, re.VERBOSE)

        P_TAG = re.compile(r"""
        <([A-Z]{1,9})>  # Match any upper case letter with length 1 to 9
        [^<]*           # Match any letter other than <
        </\1>           # Match the close tag with the same tag name
        """, re.VERBOSE)

        # First replace any CDATA string or 't' char with '-'.
        curr = re.sub(P_CDATA, '-', code)

        # Then check any tags if valid.
        prev = None
        while curr != prev:
            prev, curr = curr, re.sub(P_TAG, 't', curr)

        return curr == 't'  # Check if all tags are matched.


print(Solution().isValid('<DIV><DIV>123</DIV>456<DIV>789</DIV></DIV>'))
