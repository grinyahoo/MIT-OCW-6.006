# Binary Search Tree data structure implementation
# for MIT 6006 problem set 3

class BSTree(object):

    def __init__(self, array, root = None, parent = None):
        """ Creates BSTree from sorted by key array of Objects. Array should have unique keys
        """

        if len(array) == 0:
            raise Exception("tree construction error: array is empty" + repr(array) + " parent: " + repr(parent))

        if root is not None:
            self.root = root
        else:
            self.root = self

        self.key = array[len(array)//2][0]
        if type(array[len(array)//2][1]) is list:
            self.value = array[len(array)//2][1]
        else:
            self.value = [array[len(array)//2][1]]
        self.parent = parent
        self.right = None
        self.left = None

        if len(array[:len(array)//2]) > 0:
            self.left = BSTree(array[:len(array)//2], self.root, self)
        if len(array[len(array)//2 + 1:]) > 0:
            self.right = BSTree(array[len(array)//2 + 1:], self.root, self)

    def __repr__(self):

        if self.key is None:
            return "None key"
        else:
            output = "Node: " + repr(self.key) + " => " + repr(self.value) + "\n"
            # output += "Left: " + repr(self.left) + "\n"
            # output += "Right: " + repr(self.right) + "\n"
            return output

    def treeRoot(self):
        """ Returns root of the Tree """
        return self.root

    def getParent(self):
        """ Returns parent or None if root"""
        return self.parent

    def findByKey(self, key, lowerBound = False, upperBound = False):
        """ Find a node by key in tree."""
        # if key is not present returns None
        # if key is not present and lowerBound is set returns next node with key greater than given
        # if key is not present and upperBound is set returns previous node with key smaller than given
        # lowerBound and upperBound can't be set at the same call

        if self.key is None:
            return None
        if self.key == key:
            return self
        if self.key > key and self.left is not None:
            return self.left.findByKey(key, lowerBound, upperBound)
        if self.key < key and self.right is not None:
            return self.right.findByKey(key, lowerBound, upperBound)

        if lowerBound:
            if self.key > key:
                return self
            else:
                return self.nextNode()
        if upperBound:
            if self.key < key:
                return self
            else:
                return self.prevNode()

    def insert(self, key, value, deligatedFromRoot = False):
        """ Inserts node in Tree"""

        if self is self.root or deligatedFromRoot:
            if self.key == key:
                self.value.append(value)

            if self.key > key:
                if self.left is None:
                    self.left = BSTree([[key, value]], self.root, self)
                else:
                    self.left.insert(key, value, True)
            if self.key < key:
                if self.right is None:
                    self.right = BSTree([[key, value]], self.root, self)
                else:
                    self.right.insert(key, value, True)
        else:
            raise Exception("Insert can't be initiated from subtree!")


    def delete(self, key):
        """ Deletes node from Tree """

        node = self.findByKey(key)

        if node.left is None or node.right is None:
            if node.isLeftChild():
                node.parent.left = node.left or node.right
                if node.parent.left is not None:
                    node.parent.left.parent = node.parent
            else:
                node.parent.right = node.left or node.right
                if node.parent.right is not None:
                    node.parent.right.parent = node.parent

        else:
            candidate = node.nextNode()
            if candidate is not None:
                node.key, node.value = candidate.key, candidate.value
                candidate.delete()
            else:
                candidate = node.prevNode()
                if candidate is not None:
                    node.key, node.value = candidate.key, candidate.value
                    candidate.delete()

    def isLeftChild(self):
        return self.parent and self.parent.left and self.parent.left is self

    def isRightChild(self):
        return self.parent and  self.parent.right and self.parent.right is self

    def nextNode(self, key = None):
        """ Returns successor by key or None if missing"""

        if key is not None:
            node = self.findByKey(key)
        else:
            node = self

        if node.right is None:
            if node.isLeftChild():
                return node.parent
            if node.isRightChild():
                candidate = node.parent
                while candidate.isRightChild():
                    candidate = candidate.parent
                return candidate.parent
        else:
            return node.right.minNode()

    def prevNode(self, key = None):
        """ Returns predecessor by key or None if missing"""

        if key is not None:
            node = self.findByKey(key)
        else:
            node = self

        if node.left is None:
            if node.isRightChild():
                return node.parent
            if node.isLeftChild():
                candidate = node.parent
                while candidate.isLeftChild():
                    candidate = candidate.parent
                return candidate.parent
        else:
            return node.left.maxNode()

    def maxNode(self):
        """ Returns maximum of Tree"""
        if self.right is None:
            return self
        else:
            return self.right.maxNode()

    def minNode(self):
        """ Returns minimum of Tree"""
        if self.left is None:
            return self
        else:
            return self.left.minNode()

    def displayTree(self, level = 0, arr = None):
        if arr is None:
            arr = [[]]
        if len(arr) < level + 1:
            for x in xrange(len(arr)-1,level):
                arr.append([])

        arr[level].append(self.key)
        if self.left is not None:
            arr = self.left.displayTree(level + 1, arr)

        if self.right is not None:
            arr = self.right.displayTree(level + 1, arr)

        output = arr
        arr = None
        return output
