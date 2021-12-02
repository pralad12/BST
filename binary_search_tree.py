
class BSTNode():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.rightChild = None
        self.leftChild = None

    def setLeftChild(self, other):
        self.leftChild = other

    def setRightChild(self, other):
        self.rightChild = other

    def hasLeftChild(self):
        if self.leftChild is not None:
            return True
        return False

    def hasRightChild(self):
        if self.rightChild is not None:
            return True
        return False

    def put(self, key, value):
        if self.key == key:
            self.value = value
        elif self.key > key:
            if self.hasLeftChild():
                self.leftChild.put(key, value)
            else:
                self.leftChild = BSTNode(key, value)
        else:
            if self.hasRightChild():
                self.rightChild.put(key, value)
            else:
                self.rightChild = BSTNode(key, value)

    def hasKey(self, key):
        if self.key == key:
            return True
        elif self.key > key:
            if self.hasLeftChild():
                return self.leftChild.hasKey(key)
            else:
                return False
        else:
            if self.hasRightChild():
                return self.rightChild.hasKey(key)
            else:
                return False

    def get(self, key):
        if self.key == key:
            return self.value
        elif self.key > key:
            if self.hasLeftChild():
                return self.leftChild.get(key)
            else:
                return None
        else:
            if self.hasRightChild():
                return self.rightChild.get(key)
            else:
                return None

    def remove(self, key):

        if self.key == key:
            if not self.hasLeftChild() and not self.hasRightChild():
                return None
            if self.hasLeftChild() and not self.hasRightChild():
                return self.leftChild
            if self.hasRightChild() and not self.hasLeftChild():
                return self.rightChild
            # if both children
            if self.hasRightChild() and self.hasLeftChild():
                pointer = self.rightChild
                while pointer.hasLeftChild():
                    pointer = pointer.leftChild

                self.value = pointer.value
                self.key = pointer.key
                self.rightChild = self.rightChild.remove(self.key)


        elif self.key > key:
            if self.hasLeftChild():
                self.leftChild = self.leftChild.remove(key)
        else:

            if self.hasRightChild():
                self.rightChild = self.rightChild.remove(key)

        return self


# Binary Tree class
class BSTree():
    def __init__(self):
        self.size = 0
        self.root = None

    # Returns the size of the tree
    def size(self):
        return self.size

    # Checks to see if a key is in the tree
    def hasKey(self, key):
        if self.root is None:
            return False
        elif self.root.key == key:
            return True
        else:
            return self.root.hasKey(key)

    def put(self, key, value):
        if self.root is None:
            self.root = BSTNode(key, value)
            self.size += 1
        elif self.root.key == key:
            self.root.value = value
        else:
            self.root.put(key, value)
            self.size += 1

    def get(self, key):
        if self.root is None:
            return None
        elif self.root.key == key:
            return self.root.value
        else:
            return self.root.get(key)

    def remove(self, key):
        if self.root is None:
            return
        else:
            self.root = self.root.remove(key)



