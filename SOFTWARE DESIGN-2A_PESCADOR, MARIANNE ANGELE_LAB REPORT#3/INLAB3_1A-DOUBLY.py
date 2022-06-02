class Node:
    def __init__(self, data):
        self.previous = None
        self.data = data
        self.next = None
 
 
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.start_node = None
        self.last_node = None
 
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            new_node = Node(data)
            self.last_node.next = new_node
            new_node.previous = self.last_node
            new_node.next = None
            self.last_node = new_node
 
    def display(self, Type):
        if Type == 'Left_To_Right':
            current = self.head
            while current is not None:
                print(current.data, end=' ')
                current = current.next
            print()
        else:
            current = self.last_node
            while current is not None:
                print(current.data, end=' ')
                current = current.previous
            print()
 
 
if __name__ == '__main__':
    L = DoublyLinkedList()
    L.append(1)
    L.append(2)
    L.append(3)
    L.append(4)
    L.display('Left_To_Right')
    L.display('Right_To_Left')