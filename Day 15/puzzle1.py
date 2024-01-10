# implementing as a linked list for basic data structure practice


i = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7".split(',')


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node




    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
 
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
 
        current_node.next = new_node

    def hashAlgorithm(self):
        tot = 0
        
        # set the current node at the beginning of the list
        current_node = self.head
        
        
        
        # iterate until the current node becomes None
        while(current_node):
            # calculate a value for each character in the string
            
            print(current_node.data)
            curr = 0
            for c in list(current_node.data):
                curr = ((curr + ord(c)) * 17) % 256
                print(c)
                print(str(((ord(c) * 17) % 256)))
            current_node = current_node.next
            print()
            tot+= curr
        
        print(tot)

# create the list
llist = LinkedList()

# append each value to the list
for x in i:
     llist.insertAtEnd(x)

llist.hashAlgorithm()