"""
https://leetcode.com/problems/encode-and-decode-tinyurl/
"""


from random import choice
from string import ascii_letters, digits


class Codec:
    """
    Generate a 6 chars code by picking each char from 'a-zA-Z0-9', which gives
    us (10 + 26 + 26) ^ 6 combinations. This is better than using an integer
    because of the below reasons:
    1. When the same url is encoded several times, the integer code will
        generate duplicate entries.
    2. The integer combination could be easily tried by the user to get other
        encoded urls.

    If the code length is not sufficient, we could then increase the code
    length to prevent generating the same code from the choice function.
    """

    _OPTIONS = ascii_letters + digits
    _CODE_LEN = 6
    _PREFIX = 'http://tinyurl.com/'

    def __init__(self):
        self.urlToCode = {}
        self.codeToUrl = {}

    def encode(self, longUrl: str) -> str:
        if longUrl not in self.urlToCode:
            code = ''.join(
                choice(self._OPTIONS) for _ in range(self._CODE_LEN))
            while code in self.codeToUrl:
                code = ''.join(
                    choice(self._OPTIONS) for _ in range(self._CODE_LEN))

            self.urlToCode[longUrl] = code
            self.codeToUrl[code] = longUrl

        return '/'.join([self._PREFIX, self.urlToCode[longUrl]])

    def decode(self, shortUrl: str) -> str:
        return self.codeToUrl[shortUrl[-self._CODE_LEN:]]
