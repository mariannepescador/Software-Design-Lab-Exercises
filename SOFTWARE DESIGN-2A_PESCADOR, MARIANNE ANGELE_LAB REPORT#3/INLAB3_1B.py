
class Node:  
    def __init__(self):      
        self.coeff = None
        self.power = None
        self.next = None
  
def addnode(start, coeff, power):

    newnode = Node();
    newnode.coeff = coeff;
    newnode.power = power;
    newnode.next = None;
  
    if (start == None):
        return newnode;

    ptr = start;
    while (ptr.next != None):
        ptr = ptr.next;
    ptr.next = newnode;
    return start;

def printList(ptr):
 
    while (ptr.next != None):
        print(str(ptr.coeff) + 'x^' + str(ptr.power), end = '')
        if( ptr.next != None and ptr.next.coeff >= 0):
            print('+', end = '')
        ptr = ptr.next
    print(ptr.coeff)
      
def removeDuplicates(start):
    ptr2 = None
    dup = None
    ptr1 = start;

    while (ptr1 != None and ptr1.next != None):
        ptr2 = ptr1;
  
        while (ptr2.next != None):

            if (ptr1.power == ptr2.next.power):

                ptr1.coeff = ptr1.coeff + ptr2.next.coeff;
                dup = ptr2.next;
                ptr2.next = ptr2.next.next;
             
            else:
                ptr2 = ptr2.next;
         
        ptr1 = ptr1.next;

def multiply(poly1, Npoly2, poly3):
  
    ptr1 = poly1;
    ptr2 = poly2;
     
    while (ptr1 != None):
        while (ptr2 != None):
  
            coeff = ptr1.coeff * ptr2.coeff;

            power = ptr1.power + ptr2.power;

            poly3 = addnode(poly3, coeff, power);
  
            ptr2 = ptr2.next;

        ptr2 = poly2;

        ptr1 = ptr1.next;

    removeDuplicates(poly3);
    return poly3;

if __name__=='__main__':
    poly1 = None
    poly2 = None
    poly3 = None;

    poly1 = addnode(poly1, 1, 3);
    poly1 = addnode(poly1, 2, 4);
    poly1 = addnode(poly1, -5, 6);
  
    poly2 = addnode(poly2, 7, 8);
    poly2 = addnode(poly2, -9, 10);
    poly2 = addnode(poly2, 11, 12);
    poly2 = addnode(poly2, 13, 14);

    print("1st Polynomial:- ", end = '');
    printList(poly1);

    print("2nd Polynomial:- ", end = '');
    printList(poly2);

    poly3 = multiply(poly1, poly2, poly3);

    print("Resultant Polynomial:- ", end = '');
    printList(poly3);








