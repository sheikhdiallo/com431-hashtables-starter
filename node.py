class Node:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.value = value

    def link(self, othernode):
        self.next = othernode
        othernode.prev = self

    def __str__(self):
        return f"Node containing {self.value}"

