from _avl import *

tree = AVLTree()

node = Node(1,'a')
tree.insert(node)

node = Node(8,'b')
tree.insert(node)

node = Node(4,'c')
tree.insert(node)

print tree.displayTree()

for x in xrange(1,4):
	tree.delete(tree.root)
	print tree.root	
	# print tree.displayTree()

for x in xrange(10,20):
	tree.insert(Node(x, 'x'))

n = tree.findByKey(16)
tree.delete(n)




print tree.displayTree()