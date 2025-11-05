from node import Node

class TuplesLinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, key, value):
        n = Node((key ,value))
        if self.first is None:
            self.first = n
            self.last = n
        else:
            self.last.link(n)
            self.last = n

    def get(self, index):
        counter = 0
        currentNode = self.first
        while currentNode is not None:
            if counter == index:
                return currentNode
            else:
                currentNode = currentNode.next
                counter += 1
        return None
def find(self, key):
    currentNode = self.first
    while currentNode is not None:
        # currentNode.value is the tuple (key, value)
        # Used if else to check if the first element of the tuple matches the key
        if currentNode.value[0] == key:
            return currentNode.value[1]
        else:
            currentNode = currentNode.next
    return None

def __str__(self):
    contents = []
    current_node = self.first
    while current_node is not None:
        contents.append(current_node.value)
        current_node = current_node.next

    return contents.__str__()

