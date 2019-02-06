class Cache(object):

    def __init__(self, capacity_max):
        self.capacity_max = capacity_max
        self.data = {}
        self.order_list = []

    def get(self, key):
        self.rearrange_order(key)
        return self.data[key]

    def add(self, key, value):
        self.rearrange_order(key)
        self.ensure_capacity()
        self.data[key] = value 

    def rearrange_order(self, key):
        if key in self.data:
            self.order_list.remove(key)

        self.order_list.append(key)

    def ensure_capacity(self): 
        if len(self.data) < self.capacity_max: 
            return
        else:
            del self.data[self.order_list[0]]
            self.order_list.pop(0)
            

class Node(object):

    def __init__(self, data):
        # pointer = next
        self.data = data
        self.next = None
        self.tail = None

class LinkedList(object):

    def __init__(self):
        self.head = head
    
    def add_node(self, data):
        # Remember order of pointer reassignment
        # 
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

    def add_node_position(self, previous, data):
        # Inserts node after node with given data
        previous = None

        # Consider the case where previous is None - this means head node
        # Update new_node head with pointer to old head node
        
        if previous is None:
            print("No previous node!")
            return

        new_node = Node(data)
        new_node.next = previous.next
        previous.next = new_node

    def add_to_end(self, data)

        current = self.head
        new_node = Node(data)

        # Consider the case where the list is empty - new node will be the "end" & head
        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node

    def remove_node(self, data):
        # removes node with given data
        
        if self.head is not None and self.head == data:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return
        current = self.head


    def find_node(self, data):
        current = self.head

        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def remove_this_node(self, data):
        # Traverse until finding node with data 
        current = self.head
        
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False