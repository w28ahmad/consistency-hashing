'''
Binary trees are only efficient if they are balanced

- worst case insertions can take up to O(n^2) time
- where as hight balanced trees require O(nlogn) time

Defs:
- Tree Height : Maximum length of path from root to leaf
- Height Invariant: at any node the heights of left and
                    right subtrees must at most differ by 1

To balance the trees we often need to consider left and right
rotations.

Left Rotation

Before:
   10
  /  \
 5    15
     /  \
    13   20

After:
    15
   /  \
  10   20
 /  \
5   13


Right Rotation

Before:
   20
  /  \
 15   25
/  \
10  18

After:
    15
   /  \
  10   20
      /  \
     18   25
'''

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.height = 0

class AVLTree:
    def __init__(self, root=None):
        self.root = root

    def find(self, key):
        def findHelper(key, parent):
            if parent == None:
                return None
            if parent.key == key:
                return parent
            if key > parent.key:
                return findHelper(key, parent.right)
            return findHelper(key, parent.left)
        return findHelper(key, self.root)

    def insert(self, key):
        def insertHelper(key, parent):
            if parent == None:
                self.root = Node(key)
                return self.root

            if key > parent.key:
                if parent.right == None:
                    parent.right = Node(key)
                else:
                    insertHelper(key, parent.right)
                    parent = self.reBalanceRight(parent)
                    self.fixHeight(parent)
            else:
                if parent.left == None:
                    parent.left = Node(key)
                else:
                    insertHelper(key, parent.left)
                    parent = self.reBalanceLeft(parent)
                    self.fixHeight(parent)

            parent.height = max(self.checkAndGetHeight(parent.left), \
                    self.checkAndGetHeight(parent.right)) + 1
            return parent
        self.root = insertHelper(key, self.root)

    def isHeightValid(self, node):
        if node == None:
            return True

        expectedHeight = node.left.height if node.left else -1
        if node.right:
            expectedHeight = max(expectedHeight, node.right.height)

        return expectedHeight+1 == node.height and \
                self.isHeightValid(node.left) and \
                self.isHeightValid(node.right)

    def isBalanced(self, node):
        if node == None:
            return True

        leftHeight = rightHeight = 0
        if node.left:
            leftHeight = node.left.height
        if node.right:
            rightHeight = node.right.height

        return abs(leftHeight - rightHeight) <= 1

    def isOrdered(self, node, min=-float('inf'), max=float('inf')):
        if not node:
            return True

        return min <= node.key < max and \
                self.isOrdered(node.left, min, node.key) and \
                self.isOrdered(node.right, node.key, max)

    def isValid(self, node):
       return self.isOrdered(node) and \
               self.isHeightValid(node) and \
               self.isBalanced(node)

    def reBalanceLeft(self, node):
        if self.isSubtreeHeightDifferenceTwo(node):
            if self.checkAndGetHeight(node.left.left) > \
                    self.checkAndGetHeight(node.left.right):
                node = self.rotateRight(node)
            else:
                node.left = self.rotateLeft(node.left)
                node = self.rotateRight(node)
#        else:
#            self.fixHeight(node)
        return node

    def reBalanceRight(self, node):
        if self.isSubtreeHeightDifferenceTwo(node):
            if self.checkAndGetHeight(node.right.right) > \
                    self.checkAndGetHeight(node.right.left):
                node = self.rotateLeft(node)
            else:
                node.right = self.rotateRight(node.right)
                node = self.rotateLeft(node)
#        else:
#            self.fixHeight(node)
        return node

    def isSubtreeHeightDifferenceTwo(self, node):
        return abs(self.checkAndGetHeight(node.left) - \
                self.checkAndGetHeight(node.right)) == 2

    def fixHeight(self, node):
        if node == None:
            return -1

        leftHeight = self.fixHeight(node.left)
        rightHeight = self.fixHeight(node.right)
        node.height = max(leftHeight, rightHeight) + 1
        return node.height

    def checkAndGetHeight(self, node):
        if node == None:
            return -1
        return node.height

    def rotateLeft(self, parent):
        newParent = parent.right
        parent.right = newParent.left
        newParent.left = parent
        return newParent

    def rotateRight(self, parent):
        newParent = parent.left
        parent.left = newParent.right
        newParent.right = parent
        return newParent


