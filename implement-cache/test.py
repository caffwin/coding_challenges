class Node(object):

    def __init__(self, data):
        # pointer = next
        self.data = data
        self.next = None

class LinkedList(object):

    def __init__(self):
        self.head = None
    
    def add_node(self, data):
        # Remember order of pointer reassignment
        new_node = Node(data) 
        # current = self.head 

        if self.head is None: # First consideration: if list is empty
            self.head = new_node
            return 
        # traverse through list until current.next = None
        self.head = current 
        while current is not None: # while node exists
            # loop until next is null
            current = current.next
            
        current.next = new_node
    
    def print_list(self):

        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

