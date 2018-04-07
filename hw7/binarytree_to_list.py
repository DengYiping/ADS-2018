from linkedlist import Node
from binarytree import TreeNode

def treeToList(root):
    """
    This function will convert a tree into linkedlist
    >>> tree = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(9))
    >>> lst = treeToList(tree)
    >>> lst.data
    2
    >>> lst = lst.next
    >>> lst.data
    3
    >>> lst = lst.next
    >>> lst.data
    4
    >>> lst = lst.next
    >>> lst.data
    5
    >>> lst = lst.next
    >>> lst.data
    9
    """
    # basic reversed in-order traversal of BST
    # first right node, then current, then left
    rst = None # the result

    def tranverse(node):
        nonlocal rst #capture the variable rst
        if node is None:
            return 
        tranverse(node.right)
        rst = Node(node.data, rst) #append the result
        tranverse(node.left)

    tranverse(root)
    return rst
