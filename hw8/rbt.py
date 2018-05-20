class Color:
    RED = 0
    BLACK = 1

class Node:
    def __init__(self):
        self.data = None
        self.color = Color.RED
        self.left = None
        self.right = None
        self.parent = None
def printTree(rootnode):
    thislevel = [rootnode]
    a = '                                 '
    while thislevel:
        nextlevel = list()
        a = a[:len(a)//2]
        s = ''
        for n in thislevel:
            color = 'B'
            if n is not None and n.color == Color.RED:
                color = 'R'
            s = s + a + str(n.data) + color
            if n is not None and n != RedBlackTree.nil:
                nextlevel.append(n.left)
                nextlevel.append(n.right)
        print(s)
        thislevel = nextlevel


class RedBlackTree:
    nil = Node()
    nil.color = Color.BLACK


    def __init__(self):
        self.root = RedBlackTree.nil

    def rotateLeft(self, x):
        y = x.right #set y
        x.right = y.left
        if y.left != RedBlackTree.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == RedBlackTree.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def rotateRight(self, y):
        x = y.left #set x

        y.left = x.right # turn x's right subtree into y's left subtree
        if x.right != RedBlackTree.nil:
            x.right.parent = y
        x.parent = y.parent #fix parent
        if y.parent == RedBlackTree.nil:
            #fix root
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        x.right = y
        y.parent = x

    def rbInsertFixup(self, z):
        while z.parent.color == Color.RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == Color.RED:
                    z.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    z = z.parent.parent
                elif z == z.parent.right:
                    z = z.parent
                    self.rotateLeft(z)
                    z.parent.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    self.rotateRight(z.parent.parent)
                else:
                    z.parent.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    self.rotateRight(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == Color.RED:
                    z.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.rotateRight(z)
                    z.parent.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    self.rotateLeft(z.parent.parent)
            # printTree(self.root)
        self.root.color = Color.BLACK
        # printTree(self.root)

    def transplant(self, u, v):
        if u.parent == RedBlackTree.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != RedBlackTree.nil:
            v.parent = u.parent

    def rbInsert(self, z):
        y = RedBlackTree.nil
        x = self.root

        #locate the node to insert into
        while x != RedBlackTree.nil:
            y = x
            if z.data < x.data:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == RedBlackTree.nil:
            self.root = z
        elif z.data < y.data:
            y.left = z
        else:
            y.right = z

        z.left = RedBlackTree.nil
        z.right = RedBlackTree.nil
        z.color = Color.RED
        # printTree(self.root)
        self.rbInsertFixup(z)

    def insert(self, data):
        node = Node()
        node.data = data
        self.rbInsert(node)

    def rbDeleteFixup(self, x):
        while x != self.root and x.color == Color.BLACK:
            if x == x.parent.left:
                # if it == left child
                w = x.parent.right
                if w.color == Color.RED:
                    w.color = Color.BLACK
                    x.parent.color = Color.RED
                    self.rotateLeft(x.parent)
                    w = x.parent.right
                if w.left.color == Color.BLACK and w.right.color == Color.BLACK:
                    w.color = Color.RED
                    x = x.parent
                else:
                    if w.right.color == Color.BLACK:
                        w.left.color = Color.BLACK
                        w.color = Color.RED
                        self.rotateRight(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = Color.BLACK
                    w.right.color = Color.BLACK
                    self.rotateLeft(x.parent)
                    x = self.root
            else:
                # if it == right child
                w = x.parent.left
                if w.color == Color.RED:
                    w.color = Color.BLACK
                    x.parent.color = Color.RED
                    self.rotateRight(x.parent)
                    w = x.parent.left
                if w.right.color == Color.BLACK and w.left.color == Color.BLACK:
                    w.color = Color.RED
                    x = x.parent
                else:
                    if w.left.color == Color.BLACK:
                        w.right.color = Color.BLACK
                        w.color = Color.RED
                        self.rotateLeft(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = Color.BLACK
                    w.left.color = Color.BLACK
                    self.rotateRight(x.parent)
                    x = self.root
            x.color = Color.BLACK


    def deleteNode(self, z):
        y = z
        y_original_color = y.color
        if z.left == RedBlackTree.nil:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == RedBlackTree.nil:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = treeMinimun(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == Color.BLACK:
            self.rbDeleteFixup(x)

    def treeMinimum(x):
        while x.left != RedBlackTree.nil:
            x = x.left
        return x

    def treeMaximum(x):
        while x.right != RedBlackTree.nil:
            x = x.right
        return x

    def predecessor(self, x):
        if x.left != RedBlackTree.nil:
            return treeMaximum(x.left)
        y = x.parent
        while y != RedBlackTree.nil and x == y.left:
            x = y
            y = y.parent
        return y

    def successor(self, x):
        if x.right != RedBlackTree.nil:
            return treeMinimum(x.right)
        y = x.parent
        while y != RedBlackTree.nil and x == y.right:
            x = y
            y = y.parent
        return y

    def getMinimum(self):
        return treeMinimum(self.root)

    def getMaximum(self):
        return treeMaximum(self.root)

    def search(self, element):
        node = self.root
        while node != RedBlackTree.nil:
            if element == node.data:
                return node
            elif element < node.data:
                node = node.left
            else:
                node = node.right
        return RedBlackTree.nil

