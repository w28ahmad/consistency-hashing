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

'''


class Node:
    def __init__(self, key, left=None, right=None, data=None):
        self.key = key
        self.left = left
        self.right = right
        self.data = data
        self.height = 0


class AVLTree:
    def __init__(self, root=None):
        self.root = root

    def find(self, key):
        def findHelper(key, parent):
            if parent is None:
                return None
            if parent.key == key:
                return parent
            if key > parent.key:
                return findHelper(key, parent.right)
            return findHelper(key, parent.left)
        return findHelper(key, self.root)

    def insert(self, key, data=None):
        def insertHelper(key, parent):
            if parent is None:
                self.root = Node(key, data=data)
                return self.root

            if key > parent.key:
                if parent.right is None:
                    parent.right = Node(key, data=data)
                else:
                    parent.right = insertHelper(key, parent.right)
                    parent = self.reBalanceRight(parent)
                    parent.height = self.fixHeight(parent)
            else:
                if parent.left is None:
                    parent.left = Node(key, data=data)
                else:
                    parent.left = insertHelper(key, parent.left)
                    parent = self.reBalanceLeft(parent)
                    parent.height = self.fixHeight(parent)

            self.updateNodeHeight(parent)
            return parent
        self.root = insertHelper(key, self.root)

    def getNodesWithSmallerKeys(self, key):
        queue = [self.root]
        smallerNodes = []

        while queue:
            node = queue.pop()
            if not node:
                continue
            if node.key > key:
                queue.append(node.left)
            elif node.key == key:
                smallerNodes.append(node)
                queue.append(node.left)
            else:
                smallerNodes.append(node)
                queue.append(node.left)
                queue.append(node.right)
        return smallerNodes

    def getNodesWithInvalidKeys(self, key):
        queue = [self.root]
        invalidNodes = []

        while queue:
            node = queue.pop()
            if not node:
                continue
            if node.key > key:
                invalidNodes.append(node)
                queue.append(node.right)
                queue.append(node.left)
            elif node.key == key:
                queue.append(node.right)
            else:
                queue.append(node.right)

        return invalidNodes

    def getSmallestNode(self):
        currentSmallest = self.root
        while currentSmallest and currentSmallest.left:
            currentSmallest = currentSmallest.left
        return currentSmallest

    def isSmallestNode(self, key):
        if self.root is None:
            print("No nodes found")
            return
        return self.getSmallestNode().key == key

    def getSuccessorByKey(self, key):

        def getSuccessorByKeyHelper(node, key, parent):
            # Basecases
            if not node:
                if parent and parent.key > key:
                    return parent
                return None

            # Recursion
            if parent and node.key < key < parent.key:
                return getSuccessorByKeyHelper(node.right, key, node) \
                        or parent
            if parent and parent.key < key < node.key:
                return getSuccessorByKeyHelper(node.left, key, node) \
                        or parent

            if node.key == key:
                return node
            elif node.key > key:
                return getSuccessorByKeyHelper(node.left, key, node)
            else:
                return getSuccessorByKeyHelper(node.right, key, node)
        return getSuccessorByKeyHelper(self.root, key, None)

    def getSuccessorByNode(self, node):
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node

        lastLeftTurnAncestor = None
        currentRoot = self.root
        while currentRoot:
            if currentRoot.key == node.key:
                break
            elif node.key > currentRoot.key:
                currentRoot = currentRoot.right
            else:
                lastLeftTurnAncestor = currentRoot
                currentRoot = currentRoot.left
        assert currentRoot is not None, "node should always be found in tree"

        return lastLeftTurnAncestor

    def delete(self, key):
        def deleteHelper(key, node):
            if node is None:
                return None
            if node.key == key:
                hasLeftNode = node.left is not None
                hasRightNode = node.right is not None

                if hasLeftNode and hasRightNode:
                    successor = self.getSuccessorByNode(node)
                    successor.right = deleteHelper(successor.key, node.right)
                    successor.left = node.left
                    successor = self.reBalanceLeft(successor)
                    successor.height = self.fixHeight(successor)
                    return successor
                elif hasLeftNode:
                    return node.left
                elif hasRightNode:
                    return node.right
                else:
                    return None
            elif key > node.key:
                node.right = deleteHelper(key, node.right)
                node = self.reBalanceLeft(node)
                node.height = self.fixHeight(node)
            else:
                node.left = deleteHelper(key, node.left)
                node = self.reBalanceRight(node)
                node.height = self.fixHeight(node)

            self.updateNodeHeight(node)
            return node
        self.root = deleteHelper(key, self.root)

    def updateNodeHeight(self, node):
        node.height = max(self.checkAndGetHeight(node.left), \
            self.checkAndGetHeight(node.right)) + 1
        return node

    def isHeightValid(self, node):
        if node is None:
            return True

        expectedHeight = node.left.height if node.left else -1
        if node.right:
            expectedHeight = max(expectedHeight, node.right.height)

        if expectedHeight+1 != node.height:
            print(f"node with key: {node.key} expected to have height: {expectedHeight+1} but instead has height of: {node.height}")
        return expectedHeight+1 == node.height and \
                self.isHeightValid(node.left) and \
                self.isHeightValid(node.right)

    def isBalanced(self, node):
        if node is None:
            return True

        leftHeight = rightHeight = 0
        if node.left:
            leftHeight = node.left.height
        if node.right:
            rightHeight = node.right.height

        if not abs(leftHeight - rightHeight) <= 1:
            print(f"node with key {node.key} has a left height of: {leftHeight} and right height of: {rightHeight}")

        return abs(leftHeight - rightHeight) <= 1

    def isOrdered(self, node, min=-float('inf'), max=float('inf')):
        if node is None:
            return True

        if not (min <= node.key < max):
            print(f"node with key: {node.key} not between {min} and {max}")

        return min <= node.key < max and \
                self.isOrdered(node.left, min, node.key) and \
                self.isOrdered(node.right, node.key, max)

    def isValid(self, node):
        if node is None:
            return True

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
        return node

    def reBalanceRight(self, node):
        if self.isSubtreeHeightDifferenceTwo(node):
            if self.checkAndGetHeight(node.right.right) > \
                    self.checkAndGetHeight(node.right.left):
                node = self.rotateLeft(node)
            else:
                node.right = self.rotateRight(node.right)
                node = self.rotateLeft(node)
        return node

    def isSubtreeHeightDifferenceTwo(self, node):
        return abs(self.checkAndGetHeight(node.left) - \
                self.checkAndGetHeight(node.right)) == 2

    def fixHeight(self, node):
        if node is None:
            return -1

        leftHeight = self.fixHeight(node.left)
        rightHeight = self.fixHeight(node.right)
        node.height = max(leftHeight, rightHeight) + 1
        return node.height

    def isEmpty(self):
        return self.root is None

    def checkAndGetHeight(self, node):
        if node is None:
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

    def printTree(self, root):
        from asciitree import LeftAligned
        from collections import OrderedDict as OD

        tree = LeftAligned()

        def add_node(node):
            if node is None:
                return {}
            res = OD()
            if node.left is not None:
                res['left'] = add_node(node.left)
            if node.right is not None:
                res['right'] = add_node(node.right)
            return {node.key: res}

        print(tree(add_node(root)))
