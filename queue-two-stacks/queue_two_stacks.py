# Implement a queue with two stacks
# Behavior of stack = FILO
# [ a, b, c ] in a queue, "a" is accessed first, "c" last
# [ a, b, c ] in our in_stack, "c" is accessed first, then "b" then "a"
# Create an out stack to have access to reverse the stack to access the first
# item first rather than the last item

class QueueWithTwoStacks(object):
    
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)
    
    def dequeue(self):
        if len(self.out_stack) == 0:
            while len(self.in_stack) > 0:
                new_item = self.in_stack.pop()
                self.out_stack.append(new_item)
        
        return self.out_stack.pop()