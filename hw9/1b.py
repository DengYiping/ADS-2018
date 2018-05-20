class Node:
    def __init__(self, key = None, value = None):
        # just a nod3
        self.key = key
        self.value = value

class HashTable:
    def __init__(self):
        # with initial size of 100
        self.maxSize = 100
        self.currentSize = 0
        self.arr = [None] * self.maxSize

    def hashCode(self, key):
        # use the default hash of python
        return key.__hash__() % self.maxSize

    def insertNode(self, key, value):
        # insert a node into the hashTable
        if self.arr[self.hashCode(key)] is None:
            # if no conflict
            self.arr[self.hashCode(key)] = Node(key, value)
        else:
            # if conflict
            code = self.hashCode(key)
            while self.arr[code] is not None:
                code = code + 1
                if code >= self.maxSize:
                    raise RuntimeError("overflow")
            self.arr[code] = Node(key, value)

        # increase the size
        self.currentSize = self.currentSize + 1

    def get(self, key):
        # get the hashcode
        code = self.hashCode(key)
        if self.arr[code] is None:
            # entry no found
            return None
        else:
            # check if the key is right
            while self.arr[code].key != key:
                code = code + 1

                # if no found again
                if code >= self.maxSize or self.arr[code] is None:
                    return None
            return self.arr[code].value

    def isEmpty(self):
        return currentsize == 0
