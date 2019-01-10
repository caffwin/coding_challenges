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

class LinkedList(object):

    def __init__(self):
        self.head = head
    
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

    def remove_node(self, data):
        # removes node with given data
        # 

    def find_node(self, data):
        current = self.head