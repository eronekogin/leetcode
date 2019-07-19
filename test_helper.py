from typing import List


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None

    def __repr__(self):
        return '{0} -> {1}'.format(self.val, self.next)

    def create_node_list(
            self, start: int = None,
            stop: int = None, givenList: List[int] = None) -> 'ListNode':
        temp = self

        if givenList is None:
            for i in range(start, stop):
                temp.next = ListNode(i)
                temp = temp.next
        else:
            for i in givenList:
                temp.next = ListNode(i)
                temp = temp.next

        return self.next


class Sudoku:

    def print_board(self, board: List[List['Solution.Cell']]) -> str:
        rslt = ''
        for row in board:
            rslt += ' '.join([str(cell.value) for cell in row]) + '\n'

        print(rslt)
