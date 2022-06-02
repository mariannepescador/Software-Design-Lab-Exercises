class Node:
    def __init__(self,x):
        self.val=x
        self.next=None
def push(head,n_val):
    t = Node(n_val)
    t.next = head
    head = t
    return head
head = None
head = push(head,1)
head = push(head,2)
head = push(head,3)
head = push(head,4)
head = push(head,5)

temp = head 
if (temp == None or temp.next == None):
    print("List empty")

while (temp != None):
    if (temp.next.next == None):
        print(temp.val)
        break
    temp = temp.next