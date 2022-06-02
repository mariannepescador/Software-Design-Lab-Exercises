class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
         
    def append(self, data):

        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head

        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
             
    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()
 
 
if __name__ == '__main__':
    L = SinglyLinkedList()
    L.append(1)
    L.append(2)
    L.append(3)
    L.append(4)
    L.display()