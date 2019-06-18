# AVL Tree implementation
from bst import BSTree

class Node(object):
    """ Implements Node data structure """

    def __init__(self, key = None, value = None, right = None, left = None, parent = None):
        """ Creates an instace with paramenters given. Children limited by 2 """

        self.key = key
        self.value = value
        self.right = right
        self.left = left
        self.parent = parent

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

    def insert():
        pass



class AVLTree(BSTree):

    def __init__(self, array, root = None, parent = None):
        """ Creates AVLTree from array. Takes 1st element of the array as root, then inserts the rest"""

        if len(array) == 0:
            raise Exception("tree construction error: array is empty" + repr(array) + " parent: " + repr(parent))

        if root is not None:
            self.root = root
        else:
            self.root = self

        self.key = array[0][0]
        self.value = [array[0][1]]
        self.left, self.right, self.parent = None, None, parent
        self.height = 0

    def __repr__(self):

        if self.key is None:
            return "None key"
        else:
            output = "Node level(" + str(self.height) + "): " + repr(self.key) + " => " + repr(self.value) + "\n"
            # output += "Left: " + repr(self.leftChildHeight()) + "\n"
            # output += "Right: " + repr(self.rightChildHeight()) + "\n"
            return output

    def insert(self, key, value, deligatedFromRoot = False):
        """ Inserts node in Tree"""

        if self is self.root or deligatedFromRoot:
            if self.key == key:
                self.value.append(value)

            if self.key > key:
                if self.left is None:
                    self.left = AVLTree([[key, value]], self.root, self)
                    print "Insert: " + repr (self.left)
                    self.updateHeight()
                    self.checkInvariant()
                else:
                    self.left.insert(key, value, True)
            if self.key < key:
                if self.right is None:
                    self.right = AVLTree([[key, value]], self.root, self)
                    print "Insert: " + repr (self.right)
                    self.updateHeight()
                    self.checkInvariant()
                else:
                    self.right.insert(key, value, True)
        else:
            raise Exception("Insert can't be initiated from subtree!")

    def checkInvariant(self):
        # self.updateHeight()
        print "Invariant Check @ node: " + repr(self) + " L: " + str(self.leftChildHeight()) + " R: " + str(self.rightChildHeight())
        if abs(self.rightChildHeight() - self.leftChildHeight()) > 1:
            print "Invariant @ node: " + repr(self)
            self.rebalance()
        if self.parent:
            self.parent.checkInvariant()

    def rebalance(self):
        # self.updateHeight()
        if self.leftChildHeight() >= 2 + self.rightChildHeight():
            if self.left.leftChildHeight() >= self.left.rightChildHeight():
                self.rotateRight()
            else:
                self.left.rotateLeft()
                self.rotateRight()
        elif self.rightChildHeight() >= 2 + self.leftChildHeight():
            if self.right.rightChildHeight() >= self.right.leftChildHeight():
                self.rotateLeft()
            else:
                self.right.rotateRight()
                self.rotateLeft()



    def rotateRight(self):
        p, x, y, beta = self.parent, self.left, self, self.left.right

        print "rotateRight @ node: " + repr(self)

        if y is self.root:
            self.root.root = x

        if self.isLeftChild():
            x.parent, p.left = p, x
        elif p is None:
            x.parent = p
        else:
            x.parent, p.right = p, x

        y.parent = x
        if beta:
            beta.parent = y
        x.right, y.left = y, beta

        y.updateHeight()

    def rotateLeft(self):
        p, x, y, beta = self.parent, self.right, self, self.right.left

        print "rotateLeft @ node: " + repr(self)

        if self.isLeftChild():
            x.parent, p.left = p, x
        elif p is None:
            x.parent = p
        else:
            x.parent, p.right = p, x

        y.parent = x
        if beta:
            beta.parent = y
        x.left, y.right = y, beta

        y.updateHeight()

    def updateHeight(self):
        print "updateHeight @ node: " + repr(self)
        newHeight = max(self.rightChildHeight(), self.leftChildHeight()) + 1
        if self.height != newHeight:
            self.height = newHeight
            # self.avlInvariant = False
            print "newHeight = " + str(newHeight)
            if self.parent:
                self.parent.updateHeight()
                # print "qwe"
            # return True

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

    def delete(self, key):
        """ Deletes node from Tree """

        node = self.findByKey(key)
        if node:
            if node.left is None or node.right is None:
                if node.isLeftChild():
                    node.parent.left = node.left or node.right
                    if node.parent.left is not None:
                        node.parent.left.parent = node.parent
                else:
                    node.parent.right = node.left or node.right
                    if node.parent.right is not None:
                        node.parent.right.parent = node.parent
                node.parent.updateHeight()
                node.parent.checkInvariant()
                node = None
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



###############
###############

def TEST():
    testArray = [[1,"a"], [4, 'b'], [8,"c"], [16, "d"]]
    emptyArray = []

    testTree = AVLTree([[100,'x']])


    testTree.insert(5, 'e')
    testTree.insert(0, 'e')
    # testTree.insert(107, 'aa')
    # testTree.insert(7, 'qwe')
    # testTree.insert(2, 'e')
    # testTree.insert(3, 'aa')
    # testTree.insert(6, 'qwe')
    # testTree.insert(10, 'e')
    # testTree.insert(11, 'aa')
    # testTree.insert(17, 'qwe')

    print "root: " + repr(testTree.root)
    # print "R " + repr(testTree.right.root)
    # print "L " + repr(testTree.left.root)
    # print "LL " + repr(testTree.left.left)
    # print repr(testTree.left.right)

    print ""

#   print "Tree Root" + repr(testTree.left.left.treeRoot())
#   print "Parent " + repr(testTree.left.parent) + "OR with getter " + repr(testTree.left.getParent())
#   print "Find by key 3 " + repr(testTree.findByKey(3))
#   print "Find by key 3(u) " + repr(testTree.findByKey(3, False, True))
#   print "Find by key 3(l) " + repr(testTree.findByKey(3, True))
#   print "Find by key 4 " + repr(testTree.findByKey(4))
#   print "Find by key 1 " + repr(testTree.findByKey(1))
#   print "Find by key 0(l) " + repr(testTree.findByKey(0, True))
#   print "Find by key 5(l) " + repr(testTree.findByKey(5, True))





    # print "Check [5, 'e'] " + repr(testTree.right.right)

    # test = testTree.findByKey(16)
    # # testParent = test.getParent()
    # print "Root " + repr(testTree.left)
    # print repr(test) + " right " + repr(test.right) + " left " + repr(test.left) + " parent " + repr(test.parent)
    # print "Is test a isRightChild " + str(test.isRightChild())
    # print "Max " + repr(testTree.maxNode()) + " Min " + repr(testTree.minNode())

    # ###### nextNode, prevNode TEST

    # root = testTree.root
    # minimum = testTree.minNode()
    # maximum = testTree.maxNode()
    # test = minimum

    # print "### nextNode TEST\n"
    # print "root: " + repr(root)
    # print "Max " + repr(maximum) + " Min " + repr(minimum)

    # print "Start: " +repr(test)
    # while test != maximum:
    #   test = testTree.nextNode(test.key)
    #   print "Next: " + repr(test)

    # print "### prevNode TEST\n"
    # print "Start: " +repr(test)
    # while test != minimum:
    #   test = testTree.prevNode(test.key)
    #   print "Next: " + repr(test)


    # print "###### Delete test\n"
    # print testTree.displayTree()
    # test = testTree
    # test.delete(8)
    for level in testTree.displayTree():
        print level



if __name__ == '__main__':

    TEST()
