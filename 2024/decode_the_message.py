"""
https://leetcode.com/problems/decode-the-message/description/
"""


class Solution:
    """
    Solution
    """

    def decode_message(self, key: str, message: str) -> str:
        """
        decode message
        """
        mappings: dict[str, str] = {' ': ' '}
        curr = ord('a')
        end = ord('z')
        for c in key:
            if c in mappings:
                continue

            mappings[c] = chr(curr)
            curr += 1
            if curr > end:
                break

        return ''.join(map(lambda x: mappings[x], message))


print(Solution().decode_message("eljuxhpwnyrdgtqkviszcfmabo",
      "zwx hnfx lqantp mnoeius ycgk vcnjrdb"))
