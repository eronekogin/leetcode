class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)

    def print_node_list(self):
        x = str(self.val)
        y = self.next

        while y is not None:
            x += ' -> {0}'.format(y.val)
            y = y.next

        print(x)

    def create_node_list(self, start, stop):
        temp = self

        for i in range(start, stop):
            temp.next = ListNode(i)
            temp = temp.next

        return self.next
