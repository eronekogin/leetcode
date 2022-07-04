"""
https://leetcode.com/problems/design-browser-history/
"""


class BrowserHistory:

    def __init__(self, homepage: str):
        self.urls = [homepage]
        self.curr = 0

    def visit(self, url: str) -> None:
        self.urls[self.curr + 1:] = [url]
        self.curr = len(self.urls) - 1

    def back(self, steps: int) -> str:
        self.curr = max(0, self.curr - steps)
        return self.urls[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(len(self.urls) - 1, self.curr + steps)
        return self.urls[self.curr]
