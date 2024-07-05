"""
https://leetcode.com/problems/design-a-text-editor/description/
"""


from collections import deque


class TextEditor:
    """
    TextEditor
    """

    def __init__(self):
        self.prefix: deque[str] = deque([])
        self.suffix: deque[str] = deque([])

    def _get_left_chars(self, offset: int) -> str:
        return ''.join(
            self.prefix[i]
            for i in range(max(0, len(self.prefix) - offset), len(self.prefix))
        )

    def add_text(self, text: str) -> None:
        """
        add text
        """
        self.prefix.extend(list(text))

    def delete_text(self, k: int) -> int:
        """
        delete text
        """
        delete_cnt = 0
        while self.prefix and delete_cnt < k:
            self.prefix.pop()
            delete_cnt += 1

        return delete_cnt

    def cursor_left(self, k: int) -> str:
        """
        cursor left
        """
        move_cnt = 0
        while self.prefix and move_cnt < k:
            self.suffix.appendleft(self.prefix.pop())
            move_cnt += 1

        return self._get_left_chars(10)

    def cursor_right(self, k: int) -> str:
        """
        cursor right
        """
        move_cnt = 0
        while self.suffix and move_cnt < k:
            self.prefix.append(self.suffix.popleft())
            move_cnt += 1

        return self._get_left_chars(10)


t = TextEditor()
t.add_text('leetcode')
t.delete_text(4)
