class Node:
    # a basic implementation of linked list node in python
    def __init__(self, data = None, nxt = None):
        self.data = data
        self.next = nxt

def reverse(head):
    """
    test the reverse function
    >>> head = Node(1, Node(2, Node(3)))
    >>> rv = reverse(head)
    >>> rv.data
    3
    >>> rv = rv.next
    >>> rv.data
    2
    >>> rv = rv.next
    >>> rv.data
    1
    >>> rv.next is None
    True
    """
    # just call the helper
    prev = None
    current = head
    nxt = None
    while current is not None:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev
