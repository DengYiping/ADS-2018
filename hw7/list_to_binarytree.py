from binarytree import TreeNode
from linkedlist import Node

def listToTree(head):
    # We just simply append everything to the left node
    """
    Convert A sorted linkedlist into binary tree
    >>> lst = Node(1, Node(2, Node(3, Node(4))))
    >>> tree = listToTree(lst)
    >>> tmp = []
    >>> while tree is not None:
    ...     tmp.append(tree.data)
    ...     tree = tree.left
    >>> tmp
    [4, 3, 2, 1]
    """
    rst = None
    while head is not None:
        rst = TreeNode(head.data, rst, None) # append to the left
        head = head.next
    return rst
