# implementing as a linked list for basic data structure practice


i = "HASH".split(',')


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




    def inserAtEnd(self, data):
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

        current_node = self.head
        while(current_node):
            # iterate through each char in the string
            for c in list(current_node.data):
                
                
            
            
            current_node = current_node.next


# create the list
llist = LinkedList()

# append each value to the list
for x in i:
     llist.insertAtBegin(x)

llist.hashAlgorithm()