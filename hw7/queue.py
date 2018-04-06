from stack import Stack

class Queue:
    """
    A simple Queue using two stack
    >>> q = Queue()
    >>> q.enqueue(2)
    >>> q.enqueue(3)
    >>> q.enqueue(4)
    >>> q.dequeue()
    2
    >>> q.enqueue(5)
    >>> q.dequeue()
    3
    >>> q.dequeue()
    4
    >>> q.dequeue()
    5
    """
    def __init__(self):
        # initalize two Stack
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, data):
        # just put it into stack 2
        self.s1.push(data)

    def prepare_dequeue(self):
        # dump stack 1 into stack 2
        if self.s2.isEmpty():
            while not self.s1.isEmpty():
                self.s2.push(self.s1.pop())

    def dequeue(self):
        self.prepare_dequeue() #prepare
        if self.s2.isEmpty():
            raise Exception('Queue Underflow Exception')
        return self.s2.pop()
