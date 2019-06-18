class Node(object):
    """ Implements Node data structure """

    def __init__(self, key = None, value = None, right = None, left = None, parent = None, crossLink = None):
        """ Creates an instace with paramenters given. Children limited by 2 """
        
        self.key = key
        self.value = [value]
        self.right = right
        self.left = left
        self.parent = parent
        self.crossLink = crossLink
        self.height = 0
        self.rank = 1

    def __repr__(self):

        if self.key is None:
            return "None"
        else:
            output = "Node level(" + str(self.height) + ") rank("+ repr(self.rank) +"): " + repr(self.key) + " => " + repr(self.value) + "\n"
            # output += "Left: " + repr(self.leftChildHeight()) + "\n"
            # output += "Right: " + repr(self.rightChildHeight()) + "\n"
            return output

    def __lt__(self, other):
        # :nodoc: Delegate comparison to keys.
        return self.key < other.key
           
    def __le__(self, other):
        # :nodoc: Delegate comparison to keys.
        return self.key <= other.key

    def __gt__(self, other):
        # :nodoc: Delegate comparison to keys.
        return self.key > other.key

    def __ge__(self, other):
        # :nodoc: Delegate comparison to keys.
        return self.key >= other.key

    def __eq__(self, other):
        # :nodoc: Delegate comparison to keys.
        return self.key == other.key

    # def findByKey(self, key):
    #     pass

    def isLeftChild(self):
        # Existance of parent must be checked before call

        if self is self.parent.left:
            return True
        return False

    # def isRightChild():
    #     pass

    def delete(self):
        if self.parent:
            if self.isLeftChild():
                self.parent.left = None
            else:
                self.parent.right = None
        self = None

    def merge(self, other):
        if type(self.value) is not list:
            self.value = [self.value]
        if type(other.value) is not list:
            other.value = [other.value]

        self.value = self.value + other.value

    def updateHeight(self):
        newHeight = max(self.rightChildHeight(), self.leftChildHeight()) + 1
        if self.height != newHeight:
            self.height = newHeight

    def updateRank(self):
        if self.left:
            leftRank = self.left.rank
        else:
            leftRank = 0

        if self.right:
            rightRank = self.right.rank
        else:
            rightRank = 0

        self.rank = leftRank + rightRank + len(self.value)

    def rightChildHeight(self):
        if self.right:
            return self.right.height
        else: 
            return -1

    def leftChildHeight(self):
        if self.left:
            return self.left.height
        else:
            return -1


class AVLTree(object):

    def __init__(self, array = []):
        """ Creates AVLTree from array of Nodes. Takes 1st element of the array as root, then inserts the rest"""    

        self.root = None

        if len(array) > 0:
            for node in array:
                self.insert(node)

    def __repr__(self):

        if self.root is None:
            return "The Tree is empty"
        else:
            return repr(self.root)

    def findByKey(self, key, lowerBound = False, upperBound = False):
        """ Find a node by key in tree."""
        # if key is not present returns None
        # if key is not present and lowerBound is set returns next node with key greater than given
        # if key is not present and upperBound is set returns previous node with key smaller than given
        # lowerBound and upperBound can't be set at the same call
        if self.root is None:
            return None

        node = self.root

        while node:

            if node.key == key:
                return node
            if node.key > key:
                if node.left:
                    node = node.left
                else:
                    break
            if node.key < key:
                if node.right:
                    node = node.right
                else:
                    break
        
        if lowerBound:
            if node.key > key:
                return node
            else: 
                return self.nextNode(node)
        if upperBound:
            if node.key < key:
                return node
            else:
                return self.prevNode(node)

    def minCommonAncestor(self, lowerBound, upperBound):
        if lowerBound <= self.root:
            p = lowerBound
            while p.parent and p.parent<=upperBound:
                p = p.parent
        else:
            p = upperBound
            while p.parent and p.parent>=lowerBound:
                p = p.parent
        return p

    def rangeQty(self, lowerBound, upperBound, node = None, mca = None):
        if mca is None:
            mca = self.minCommonAncestor(lowerBound, upperBound)

        if node is None:
            node = mca

        result = 0
        if lowerBound.key<=node.key<=upperBound.key:
            result = len(node.value)
            # print "+ + " + repr(node)

        if node>=lowerBound and node.left is not None:
            result += self.rangeQty(lowerBound,upperBound,node.left, mca)
        if node<=upperBound and node.right is not None:
            result += self.rangeQty(lowerBound,upperBound,node.right,mca)

        return result

    def rangeList(self, lowerBound, upperBound, node = None, mca = None):
        if mca is None:
            mca = self.minCommonAncestor(lowerBound, upperBound)

        if node is None:
            node = mca

        result = []
        if lowerBound.key<=node.key<=upperBound.key:
            result = node.value
            # print "+ + " + repr(node)

        if node>=lowerBound and node.left is not None:
            result += self.rangeList(lowerBound,upperBound,node.left, mca)
        if node<=upperBound and node.right is not None:
            result += self.rangeList(lowerBound,upperBound,node.right,mca)

        return result


    def insert(self, node):
        """ Inserts node in Tree"""

        if self.root is None:
            self.root = node
            self.root.updateRank()
        else:
            candidate = self.root
            while candidate is not None:
                if candidate == node:
                    candidate.merge(node)
                    candidate.value.sort()
                    # candidate.value.append(node.value)
                    break
                elif candidate > node:
                    if candidate.left is None:
                        candidate.left = node
                        candidate.left.parent = candidate
                        # print "Insert: " + repr (self.left)
                        # self.updateHeight(candidate)
                        self.checkInvariant(candidate)
                        break
                       
                    else: 
                        candidate = candidate.left

                elif candidate < node:
                    if candidate.right is None:
                        candidate.right = node
                        candidate.right.parent = candidate
                        # print "Insert: " + repr (self.right)
                        # self.updateHeight(candidate)
                        self.checkInvariant(candidate)
                        break
                        
                    else:
                        candidate = candidate.right
            self.reRank(candidate)

    def reRank(self, node):
        node.updateRank()
        p = node.parent
        while p:
            p.updateRank()
            p = p.parent
            # print "&"

    def checkInvariant(self, node):
        node.updateHeight()
        # print "Invariant Check @ node: " + repr(node) + " L: " + str(node.leftChildHeight()) + " R: " + str(node.rightChildHeight())
        if abs(node.rightChildHeight() - node.leftChildHeight()) > 1:
            # print "Invariant @ node: " + repr(node)
            self.rebalance(node)
        if node.parent:
            self.checkInvariant(node.parent)

    def rebalance(self, node):
        # self.updateHeight()
        if node.leftChildHeight() >= 2 + node.rightChildHeight():
            if node.left.leftChildHeight() >= node.left.rightChildHeight():
                self.rotateRight(node)
            else:
                self.rotateLeft(node.left)
                self.rotateRight(node)
        elif node.rightChildHeight() >= 2 + node.leftChildHeight():
            if node.right.rightChildHeight() >= node.right.leftChildHeight():
                self.rotateLeft(node)
            else:
                self.rotateRight(node.right)
                self.rotateLeft(node)

    def rotateRight(self, node):
        p, x, y, beta = node.parent, node.left, node, node.left.right

        # print "rotateRight @ node: " + repr(node)

        if y is self.root:
            self.root = x

        if p:
            if y.isLeftChild():
                p.left = x
            else:
                p.right = x

        x.parent = p
        y.parent = x

        if beta:
            beta.parent = y
        x.right, y.left = y, beta

        y.updateHeight()
        self.reRank(y)
        x.updateHeight()
        self.reRank(x)

    def rotateLeft(self, node):
        p, x, y, beta = node.parent, node.right, node, node.right.left

        # print "rotateLeft @ node: " + repr(node)

        if y is self.root:
            self.root = x

        if p:
            if y.isLeftChild():
                p.left = x
            else:
                p.right = x

        x.parent = p
        y.parent = x

        if beta:
            beta.parent = y
        x.left, y.right = y, beta
        
        y.updateHeight()
        self.reRank(y)
        x.updateHeight()
        self.reRank(x)

    def delete(self, node, w = None):
        """ Deletes node from Tree """
        
        # node = self.findByKey(key)
        if node:
            if w and len(node.value) > 1:
                node.value.remove(w)
            else:
                if node.left is None or node.right is None:
                    if node.parent:
                        if node.isLeftChild():
                            node.parent.left = node.left or node.right
                            if node.parent.left is not None:
                                node.parent.left.parent = node.parent
                        else:
                            node.parent.right = node.left or node.right
                            if node.parent.right is not None:
                                node.parent.right.parent = node.parent
                        p = node.parent
                        self.checkInvariant(node.parent)
                        
                        node = None
                        self.reRank(p)
                    else:
                        if node.left:
                            node.left.parent = None
                            self.root = node.left
                        elif node.right:
                            node.right.parent = None
                            self.root = node.right
                        else:
                            self.root = None
                        node = None

                else:
                    candidate = self.nextNode(node)
                    if candidate is not None:
                        node.key, node.value = candidate.key, candidate.value
                        self.delete(candidate)
                    else:
                        candidate = self.prevNode(node)
                        if candidate is not None:
                            node.key, node.value = candidate.key, candidate.value
                            self.delete(candidate)


    def nextNode(self, node):
        """ Returns successor by key or None if missing"""
    
        if node is self.maxNode():
            return None

        if node.right is None:
            if node.parent:
                if node.isLeftChild():
                    return node.parent
                else:
                    candidate = node.parent
                    while not candidate.isLeftChild():
                        candidate = candidate.parent
                    return candidate.parent
        else:
            return self.minNode(node.right)

    def prevNode(self, node):
        """ Returns predecessor by key or None if missing"""

        if node is self.minNode():
            return None

        if node.left is None:
            if node.parent:
                if not node.isLeftChild():
                    return node.parent
                else:
                    candidate = node.parent
                    while candidate.isLeftChild():
                        candidate = candidate.parent
                    return candidate.parent
        else:
            return self.maxNode(node.left)

    def maxNode(self, node = None):
        """ Returns maximum of Tree. Returns maximum of subtree(node) if paramenter node given"""

        if node:
            m = node
        else:
            m = self.root

        while m.right:
            m = m.right

        return m

    def minNode(self, node = None):
        """ Returns minimum of Tree"""
        
        if node:
            m = node
        else:
            m = self.root

        while m and m.left:
            m = m.left

        return m

    def displayTree(self):
        arr = []
        current = self.minNode()
        while current:
            arr.append(current)
            current = self.nextNode(current)
        return arr
