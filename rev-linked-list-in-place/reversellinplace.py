"""Given linked list, reverse the nodes in this linked list in place.

Iterative solution doctest:
    
    >>> ll1 = LinkedList(Node(1, Node(2, Node(3))))
    >>> ll1.as_string()
    '123'
    >>> reverse_linked_list_in_place(ll1)
    >>> ll1.as_string()
    '321'

"""

# Recursive solution doctest:

#     >>> ll2 = LinkedList(Node(1, Node(2, Node(3))))
#     >>> ll2.as_string()
#     '123'
#     >>> reverse_linked_list_in_place_rec(ll2)
#     >>> ll2.as_string()
#     '321'
# """


class LinkedList(object):
    """Linked list."""

    def __init__(self, head=None):
        self.head = head

    def as_string(self):
        """Represent data for this list as a string.

        >>> LinkedList(Node(3)).as_string()
        '3'

        >>> LinkedList(Node(3, Node(2, Node(1)))).as_string()
        '321'
        """

        out = []
        n = self.head

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(out)


class Node(object):
    """Class in a linked list."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# Iteration solution.
def reverse_linked_list_in_place(lst):
    """Given linked list, reverse the nodes in this linked list in place."""

    previous = None # set previous to None
    current = lst.head # self.head is the only attribute

    while current is not None: # aka "while current:" (while current exists)
        next_node = current.next # set next to the node following the current node
        current.next = previous # previous also set 
        previous = current 
        current = next_node

    lst.head = previous # set head to previous node

def reverse_linked_list_in_place_rec(lst):
    """Given linked list, RECUSIVELY reverse the nodes 
    in this linked list in place."""

    current = lst.head
    previous = None

    def _rec_reverse(current, previous):
        
        #base case
        if not current:
            return previous

        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

        return _rec_reverse(current, previous)

    lst.head = _rec_reverse(current, previous)
    

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. RIGHT ON!\n")
