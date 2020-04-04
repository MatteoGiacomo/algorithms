""" Testing dynamic programming
	build_tree: build a binary tree (not perfect) with memoization where every node's value
				is a substring of the root value
	in_order_check: find out every values divisble by 3
"""

class BinaryTree(object):
    
    def __init__(self, objectKey):
        self.key = objectKey
        self.leftChild = None
        self.rightChild = None

    def insertLeftChild(self, key):
        if self.leftChild == None:
            self.leftChild = BinaryTree(key)
        else:
            temp = BinaryTree(key)
            # add reference to new node 
            temp.leftChild = self.leftChild

            # update old reference
            self.leftChild = temp

    def insertRightChild(self, key):
        if self.rightChild == None:
            self.rightChild = BinaryTree(key)
        else:
            temp = BinaryTree(key)
            # add reference to new node 
            temp.rightChild = self.rightChild

            # update old reference
            self.rightChild = temp

cache = set()


# memoization already avoid equal values so a list is enough
res = []

# ex root = BinaryTree('25738')

def build_tree(root):
	""" build a binary tree with memoization avoiding to create 
		nodes with value already present in cache
	""" 

    if len(root.key) == 1:
        return 

    else:
        lc_value = root.key[:len(root.key)-1]
        rc_value = root.key[1:]

        if lc_value not in cache:
            cache.add(lc_value)
            root.insertLeftChild(lc_value)
            build_tree(root.leftChild)

        if rc_value not in cache:
            cache.add(rc_value)
            root.insertRightChild(rc_value)  
            build_tree(root.rightChild)


def in_order_check(tree):
	""" in-order traversal checking node value divisible by 3 """

    if tree:
        in_order_check(tree.leftChild)
        if int(tree.key) % 3 == 0:
            res.append(tree.key)
        in_order_check(tree.rightChild)


