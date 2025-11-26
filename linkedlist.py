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
        currentnode = self.first
        while currentnode is not None:
            if counter == index:
                return currentnode
            else:
                currentnode = currentnode.next
                counter += 1
        return None
def find(self, key):
    currentnode = self.first
    while currentnode is not None:
        # currentNode.value is the tuple key and value
        # Used if else to check if the first element of the tuple matches the key
        if currentnode.value[0] == key:
            return currentnode.value[1]
        else:
            currentnode = currentnode.next
    return None

def __str__(self):
    contents = []
    current_node = self.first
    while current_node is not None:
        contents.append(current_node.value)
        current_node = current_node.next

    return contents.__str__()

