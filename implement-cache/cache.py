# Implement a cache with get and add methods, and an additional method that keeps track of 
# priority depending on most recently accessed items
# Consider what to do when the list reaches capacity
# Think of how to keep track of order of items, and how to rearrange upon reaching capacity

class Cache(object):

    def __init__(self, capacity_max):
        self.capacity_max = capacity_max
        self.data = {}
        self.order_list = [] # Keeps track of order of items, least to most recent

    def get(self, key):
        # Call rearrange_order, and then return the data
        self.rearrange_order(key)
        return self.data[key]

    def add(self, key, value):
        # Call rearrange_order, and then insert into the cache dict. Nothing to return. 
        # self.rearrange_order(key) # keep track of item being inserted
        self.rearrange_order(key)
        self.ensure_capacity()
        self.data[key] = value # add key/value pair to cache dict
        # self.order_list.append(key)

    def rearrange_order(self, key):
        # Reorders items based on key in self.order_list if the key already exists
        if key in self.data:
            self.order_list.remove(key)

        self.order_list.append(key)

    def ensure_capacity(self): 
        # Handles operations when cache becomes full 
        # Consider which items to remove, and how the list will be shuffled

        if len(self.data) < self.capacity_max: # if trying to add an item, reaching capacity
            # clear 
            return
        else:
            del self.data[self.order_list[0]]
            self.order_list.pop(0)
            

# When this class is created, there is an empty dictionary
# To keep track of order, create indexable list in the init
# Items can be added until reaching max capacity. Before adding, check if key already exists
# If key exists, over write in dictionary. Check list for key, and remove, then append to end.

# my_cache = Cache(3)
# my_cache.add('a', 1)  # a
# my_cache.add('b', 2)  # a b
# my_cache.add('a', 5)  # b a
# my_cache.add('c', 3)  # b a c
# c.get('b') # a c b
# c.add('d', 40) # removes a