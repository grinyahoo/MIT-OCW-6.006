# Binary Search Tree implementation
# from pprint import pprint
class Node(object):
    """ Implements Node data structure """

    def __init__(self, key = None, value = None, right = None, left = None, parent = None):
        """ Creates an instace with paramenters given. Children limited by 2 """
        
        self.key = key
        self.value = value
        self.right = right
        self.left = left
        self.parent = parent
        # self.height = 0

    def __repr__(self):

        if self.key is None:
            return "None"
        else:
            output = "Node " + repr(self.key) + " => " + repr(self.value) + "\n"
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

    # def insert():
    #     pass

    # def updateHeight(self):
    #     print "updateHeight @ node: " + repr(self)
    #     newHeight = max(self.rightChildHeight(), self.leftChildHeight()) + 1
    #     if self.height != newHeight:
    #         self.height = newHeight
    #         # self.avlInvariant = False
    #         print "newHeight = " + str(newHeight)
    #         # if self.parent:
    #         #     self.parent.updateHeight()
    #             # print "qwe"
    #         # return True

    # def rightChildHeight(self):
    #     if self.right:
    #         return self.right.height
    #     else: 
    #         return -1

    # def leftChildHeight(self):
    #     if self.left:
    #         return self.left.height
    #     else:
    #         return -1

        

class BSTree(object):

    def __init__(self, array, root = None, parent = None):
        """ Creates BSTree from sorted by key array of Objects. Array should have unique keys"""

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
        # else: 
            # arr[level].append("end")
        if self.right is not None:
            arr = self.right.displayTree(level + 1, arr)
        # else:
            # arr[level].append("end")
        output = arr
        arr = None
        return output

###############
###############

def TESTbst():
    testArray = [[1,"a"], [4, 'b'], [8,"c"], [16, "d"]]
    emptyArray = []

    testTree = BSTree(testArray)

#   print repr(testTree)
#   print repr(testTree.right)
#   print repr(testTree.left)
#   print repr(testTree.left.left)
#   print repr(testTree.left.right)

#   print "Tree Root" + repr(testTree.left.left.treeRoot())
#   print "Parent " + repr(testTree.left.parent) + "OR with getter " + repr(testTree.left.getParent())
#   print "Find by key 3 " + repr(testTree.findByKey(3))
#   print "Find by key 3(u) " + repr(testTree.findByKey(3, False, True))
#   print "Find by key 3(l) " + repr(testTree.findByKey(3, True))
#   print "Find by key 4 " + repr(testTree.findByKey(4))
#   print "Find by key 1 " + repr(testTree.findByKey(1))
#   print "Find by key 0(l) " + repr(testTree.findByKey(0, True))
#   print "Find by key 5(l) " + repr(testTree.findByKey(5, True))

    testTree.insert(5, 'e')
    testTree.insert(0, 'e')
    testTree.insert(1, 'aa')
    testTree.insert(7, 'qwe')
    # testTree.insert(2, 'e')
    # testTree.insert(3, 'aa')
    # testTree.insert(6, 'qwe')
    # testTree.insert(10, 'e')
    # testTree.insert(11, 'aa')
    # testTree.insert(17, 'qwe')
    
    

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
    print testTree.displayTree()
    # print displayTree(testTree)   


if __name__ == '__main__':

    TESTbst()








