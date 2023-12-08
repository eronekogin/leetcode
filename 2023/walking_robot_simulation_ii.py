"""
https://leetcode.com/problems/walking-robot-simulation-ii/
"""


class Robot:
    """
    Robot
    """

    def __init__(self, width: int, height: int):
        self.i = 0
        self.pos = (
            [[0, 0, 'South']] +
            [[i, 0, 'East'] for i in range(1, width)] +
            [[width - 1, i, 'North'] for i in range(1, height)] +
            [[i, height - 1, 'West'] for i in range(width - 2, -1, -1)] +
            [[0, i, 'South'] for i in range(height - 2, 0, -1)]
        )

    def step(self, num: int) -> None:
        """
        step
        """
        self.i += num

    def get_pos(self) -> list[int]:
        """
        get_pos
        """
        return self.pos[self.i % len(self.pos)][:2]

    def get_dir(self) -> str:
        """
        get_dir
        """
        return self.pos[self.i % len(self.pos)][2] if self.i > 0 else 'East'


r = Robot(6, 3)
r.step(4)
r.step(2)
r.step(1)
r.step(4)
r.get_pos()
