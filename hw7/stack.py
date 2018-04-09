class StackNode:
    """
    A basic linked list implementation
    """
    def __init__(self, data = None, nxt = None):
        self.data = data
        self.next = nxt

class Stack:
    """
    Implementation of Stack According to the code in the assignment
    >>> s = Stack(2)
    >>> s.isEmpty()
    True
    >>> s.push(5)
    >>> s.isEmpty()
    False
    >>> s.current_size
    1
    >>> s.push(4)
    >>> s.current_size
    2
    >>> s.pop()
    4
    >>> s.pop()
    5
    >>> s.isEmpty()
    True
    """
    def __init__(self, size = None):
        # there is no recursive call so constant time
        if size is None:
            self.size = -1
        elif size <= 0:
            raise Exception('Invalid size')
        else:
            self.size = size

        self.current_size = -1
        self.top = None

    def push(self, data):
        # constant time`
        # check the size
        if self.size != -1 and self.current_size == self.size:
            raise Exception('Stack Overflow Exception')

        if self.top is None:
            self.top = StackNode(data) #create a node
            self.current_size = 1 #set the proper size
        else:
            self.top = StackNode(data, self.top) #simply append the linked list
            self.current_size = self.current_size + 1 # increment

    def pop(self):
        # constant time
        if self.top is None:
            raise Exception('Stack Underflow Exception')

        val = self.top.data
        self.top = self.top.next # move to next one
        self.current_size = self.current_size - 1
        return val

    def isEmpty(self):
        # constant time
        return self.top is None

