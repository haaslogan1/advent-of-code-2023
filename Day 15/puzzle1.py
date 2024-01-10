# implementing as a linked list for basic data structure practice

# Sample input
# i = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7".split(',')


# Input
i = open("input.txt").read().strip('\n').split(',')

# Node class for each entry in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# linked list class
class LinkedList:
    # constructor
    def __init__(self):
        self.head = None

    # function to insert at the end of the linked list
    def insertAtEnd(self, data):
        # create a new node for the list
        new_node = Node(data)
        
        # if the list is empty
        if self.head is None:
            # start the list head
            self.head = new_node
        # otherwise, iterate to the end and add there
        else:
            current_node = self.head
            # move along until the next node is None
            while(current_node.next):
                current_node = current_node.next
            
            # replace the None next with this node
            current_node.next = new_node

    def hashAlgorithm(self):
        # total count
        tot = 0
        
        # set the current node at the beginning of the list
        current_node = self.head
        
        # iterate until the current node becomes None
        while(current_node):
            # calculate a value for each character in the string
            # setting current to 0
            curr = 0
            for c in list(current_node.data):
                # perfrom the day 15 outlined algorithm for this char
                curr = ((curr + ord(c)) * 17) % 256
            # iterate to the next string
            current_node = current_node.next
            
            #add to the total
            tot+= curr
        
        print(tot)

# create the list
llist = LinkedList()

# append each value to the list
for x in i:
     llist.insertAtEnd(x)

llist.hashAlgorithm()