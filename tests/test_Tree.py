from src.Tree import AVLTree, Node


def testFind():
    tree = AVLTree()
    assert tree.find(1) is None, "Find should return None for an empty tree"

    tree.insert(1)
    assert isinstance(tree.find(1), Node), "Find should return a \
            Node for existing key"
    assert tree.find(1).key == 1, "Find should return the correct Node"

    assert tree.find(2) is None, "Find should return None for non-existing key"


def testInsert():
    tree = AVLTree()

    tree.insert(1)
    assert tree.root.key == 1, "Root key should be 1 after inserting 1"
    assert tree.root.height == 0, "Root height should be 0 after inserting 1"

    tree.insert(2)
    assert tree.root.right.key == 2, "The right child of root \
            should have key 2 after inserting 2"
    assert tree.root.right.height == 0, "The right child of root \
            should have height 1 after inserting 2"
    assert tree.root.height == 1, "Root height should be 1 after inserting 2"


def testIsHeightValid():
    tree = AVLTree()

    tree.insert(1)
    assert tree.isHeightValid(tree.root), "isHeightValid should return \
            True after inserting 1"

    tree.insert(2)
    assert tree.isHeightValid(tree.root), "isHeightValid should return \
            True after inserting 2"


def testIsBalanced():
    tree = AVLTree()

    tree.insert(1)
    assert tree.isBalanced(tree.root), "isBalanced should return \
            True after inserting 1"

    tree.insert(2)
    assert tree.isBalanced(tree.root), "isBalanced should return \
            True after inserting 2"


def testComplexBinaryTreeOperations():
    tree = AVLTree()

    keysToInsert = [5, 2, 8, 1, 3, 7, 10, 4, 6, 9, 11]
    for key in keysToInsert:
        tree.insert(key)

    assert tree.root.key == 5, "The root key should be 5"
    assert tree.root.height == 3, "The root height should be 4"

    assert tree.isHeightValid(tree.root), "isHeightValid should return True"

    assert tree.isOrdered(tree.root), "isOrdered should return True"

    for key in keysToInsert:
        node = tree.find(key)
        assert isinstance(node, Node), f"Find should return a \
                Node for existing key {key}"
        assert node.key == key, f"Find should return the \
                correct Node for key {key}"

        assert tree.isBalanced(node), "isBalanced should return True"

    assert tree.find(100) is None, "Find should return \
            None for non-existing key 100"

    assert tree.isValid(tree.root), "The tree is left in a valid state"


def testBasicRightTreeInBalance():
    tree = AVLTree()

    keysToInsert = [1, 2, 3]

    for key in keysToInsert:
        tree.insert(key)

    assert tree.root.key == 2, "The root should have a value of \
            2 after balancing"
    assert tree.root.height == 1, "The root should have a height of \
            1 after balancing"
    assert tree.root.left.key == 1, "The left key is equal to 1"
    assert tree.root.right.key == 3, "The right key is equal to 3"
    assert tree.isValid(tree.root), "The tree is left in a valid state"


def testBasicLeftTreeInBalance():
    tree = AVLTree()

    keysToInsert = [3, 2, 1]

    for key in keysToInsert:
        tree.insert(key)

    assert tree.root.key == 2, "The root should have a value of \
            2 after balancing"
    assert tree.root.height == 1, "The root should have a height of \
            1 after balancing"
    assert tree.root.left.key == 1, "The left key is equal to 1"
    assert tree.root.right.key == 3, "The right key is equal to 3"
    assert tree.isValid(tree.root), "The tree is left in a valid state"


def testRightLeftInBalance():
    tree = AVLTree()

    keysToInsert = [1, 3, 2]

    for key in keysToInsert:
        tree.insert(key)

    assert tree.root.key == 2, "The root should have a \
            value of 2 after balancing"
    assert tree.root.height == 1, "The root should have a \
            height of 1 after balancing"
    assert tree.root.left.key == 1, "The left key is equal to 1"
    assert tree.root.right.key == 3, "The right key is equal to 3"
    assert tree.isValid(tree.root), "The tree is left in a valid state"


def testLeftRightInBalance():
    tree = AVLTree()

    keysToInsert = [3, 1, 2]

    for key in keysToInsert:
        tree.insert(key)

    assert tree.root.key == 2, "The root should have a value \
            of 2 after balancing"
    assert tree.root.height == 1, "The root should have a \
            height of 1 after balancing"
    assert tree.root.left.key == 1, "The left key is equal to 1"
    assert tree.root.right.key == 3, "The right key is equal to 3"
    assert tree.isValid(tree.root), "The tree is left in a valid state"


def testComplexLeftRightAndRightLeftTreeBalance():
    tree = AVLTree()

    keysToInsert = [20, 10, 30, 25, 35, 15, 5, 40, 23, 28]

    for key in keysToInsert:
        tree.insert(key)

    assert tree.root.key == 20, "Root should be 20"
    assert tree.root.left.key == 10, "20's left child should be 10"
    assert tree.root.left.left.key == 5, "10's left child should be 5"
    assert tree.root.left.right.key == 15, "10's right child should be 15"
    assert tree.root.right.key == 30, "20's right child should be 30"
    assert tree.root.right.left.key == 25, "30's left child should be 25"
    assert tree.root.right.right.key == 35, "30's right child should be 35"
    assert tree.root.right.right.right.key == 40, "35's right \
            child should be 40"

    assert tree.root.height == 3, "The tree has a height of 3"
    assert tree.isValid(tree.root), "The tree is left in a valid state"


def testRightInsertLoadTest():
    tree = AVLTree()

    keysToInsert = [i for i in range(1, 25)]

    for key in keysToInsert:
        tree.insert(key)

    assert tree.root.key == 16, "Root should be 16"
    assert tree.root.right.key == 20, "Root.right should be 20"
    assert tree.root.left.key == 8, "Root.left should be 8"
    assert tree.isValid(tree.root), "The tree is left in a valid state"


def testLeftInsertLoadTest():
    tree = AVLTree()

    keysToInsert = [i for i in range(24, 0, -1)]

    for key in keysToInsert:
        tree.insert(key)

    assert tree.root.key == 9, "Root should be 9"
    assert tree.root.right.key == 17, "Root.right should be 17"
    assert tree.root.left.key == 5, "Root.left should be 5"
    assert tree.isValid(tree.root), "The tree is left in a valid state"


def testBasicRootDeletion():
    tree = AVLTree()
    tree.insert(1)
    tree.delete(1)

    assert tree.root is None, "Root is deleted and is None"


def testBasicLeftDeletion():
    tree = AVLTree()
    tree.insert(1)
    tree.insert(2)
    tree.delete(2)

    assert tree.root.key == 1, "Root remains 1"
    assert tree.root.left is None, "Root left is None"
    assert tree.root.right is None, "Root right is removed"
    assert tree.isValid(tree.root), "The tree is left in a valid state"


def testBasicRightDeletion():
    tree = AVLTree()
    tree.insert(2)
    tree.insert(1)
    tree.delete(1)

    assert tree.root.key == 2, "Root remains 2"
    assert tree.root.right is None, "Root right is None"
    assert tree.root.left is None, "Root left is Removed"
    assert tree.isValid(tree.root), "The tree is left in a valid state"


def testRootRightReplacementDuringDeletion():
    tree = AVLTree()
    tree.insert(2)
    tree.insert(3)
    tree.insert(1)
    tree.delete(2)

    assert tree.root.key == 3, "Root is replaced by right node"
    assert tree.root.left.key == 1, "Root left is the same"
    assert tree.isValid(tree.root), "The tree is left in a valid state"


def testRootLeftReplacementDuringDeletion():
    tree = AVLTree()
    tree.insert(2)
    tree.insert(1)
    tree.delete(2)

    assert tree.root.key == 1, "Root is replaced by right node"
    assert tree.isValid(tree.root), "The tree is left in a valid state"


def testInorderDeleteLoadTest():
    tree = AVLTree()

    keysToInsertAndDelete = [i for i in range(1, 25)]

    for key in keysToInsertAndDelete:
        tree.insert(key)

    for key in keysToInsertAndDelete:
        tree.delete(key)

        assert tree.isValid(tree.root), f"The tree is left \
                valid after deleting \
                key: {key}"

    assert tree.root is None, "All nodes are removed"


def testNonInorderDeleteLoadTest():
    tree = AVLTree()

    keysToInsertAndDelete = [i for i in range(1, 25)]

    for key in keysToInsertAndDelete:
        tree.insert(key)

    for key in keysToInsertAndDelete[::-1]:
        tree.delete(key)

        assert tree.isValid(tree.root), f"The tree is left \
                valid after deleting \
                key: {key}"

    assert tree.root is None, "All nodes are removed"


def testRootDeleteLoadTest():
    tree = AVLTree()

    keysToInsert = [i for i in range(100)]

    for key in keysToInsert:
        tree.insert(key)
        assert tree.isValid(tree.root), f"The tree is left valid \
                after inserting key: {key}"

    for i in range(len(keysToInsert)):
        deletionKey = tree.root.key
        tree.delete(deletionKey)

        assert tree.isValid(tree.root), f"The tree is left valid \
                after deleting key: {deletionKey}"

    assert tree.root is None, "All nodes are removed"


def testGetSuccessorRightWeighted():
    tree = AVLTree()
    keysToInsert = [1, 2, 4, 3, 5]

    for i in keysToInsert:
        tree.insert(i)

    assert tree.isValid(tree.root), "Tree is not valid"

    successorOfOne = tree.getSuccessorByNode(tree.find(1))
    successorOfTwo = tree.getSuccessorByNode(tree.find(2))
    successorOfThree = tree.getSuccessorByNode(tree.find(3))
    successorOfFour = tree.getSuccessorByNode(tree.find(4))
    successorOfFive = tree.getSuccessorByNode(tree.find(5))

    assert successorOfOne.key == 2, "Successor of one is two"
    assert successorOfTwo.key == 3, "Successor of two is three"
    assert successorOfThree.key == 4, "Successor of three is four"
    assert successorOfFour.key == 5, "Successor of four is five"
    assert successorOfFive is None, "Successor of five is None"


def testGetSuccessorLeftWeighted():
    tree = AVLTree()
    keysToInsert = [4, 2, 5, 1, 3]

    for i in keysToInsert:
        tree.insert(i)

    assert tree.isValid(tree.root), "Tree is not valid"

    successorOfOne = tree.getSuccessorByNode(tree.find(1))
    successorOfTwo = tree.getSuccessorByNode(tree.find(2))
    successorOfThree = tree.getSuccessorByNode(tree.find(3))
    successorOfFour = tree.getSuccessorByNode(tree.find(4))
    successorOfFive = tree.getSuccessorByNode(tree.find(5))

    assert successorOfOne.key == 2, "Successor of one is two"
    assert successorOfTwo.key == 3, "Successor of two is three"
    assert successorOfThree.key == 4, "Successor of three is four"
    assert successorOfFour.key == 5, "Successor of four is five"
    assert successorOfFive is None, "Successor of five is None"


def testGetNodesWithSmallerKeys():
    tree = AVLTree()
    keysToInsert = [i for i in range(1, 101)]

    for i in keysToInsert:
        tree.insert(i)

    assert tree.isValid(tree.root), "Tree is not valid"
    nodesLessThan50 = tree.getNodesWithSmallerKeys(50)

    assert len(nodesLessThan50) == 50, "Not the correct number of nodes"
    for node in nodesLessThan50:
        assert node.key <= 50, "Key is not less than 50"


def testGetSuccessorByKey():
    tree = AVLTree()
    keysToInsert = [8, 4, 11, 2, 6, 9, 13]

    for i in keysToInsert:
        tree.insert(i)

    assert tree.isValid(tree.root), "Tree is not valid"

    successorOfOne = tree.getSuccessorByKey(1)
    successorOfTwo = tree.getSuccessorByKey(2)
    successorOfThree = tree.getSuccessorByKey(3)
    successorOfFive = tree.getSuccessorByKey(5)
    successorOfSeven = tree.getSuccessorByKey(7)
    successorOfTen = tree.getSuccessorByKey(10)
    successorOfTwelve = tree.getSuccessorByKey(12)
    successorOfFourteen = tree.getSuccessorByKey(14)

    assert successorOfOne.key == 2, "Incorrect Successor"
    assert successorOfTwo.key == 2, "Incorrect Successor"
    assert successorOfThree.key == 4, "Incorrect Successor"
    assert successorOfFive.key == 6, "Incorrect Successor"
    assert successorOfSeven.key == 8, "Incorrect Successor"
    assert successorOfTen.key == 11, "Incorrect Successor"
    assert successorOfTwelve.key == 13, "Incorrect Successor"
    assert successorOfFourteen is None, "Incorrect Successor"


def runTests():
    # Test basic BST methods
    testFind()
    testInsert()
    testIsHeightValid()
    testIsBalanced()
    testComplexBinaryTreeOperations()

    # Test Insertion Balancing
    testBasicRightTreeInBalance()
    testBasicLeftTreeInBalance()
    testRightLeftInBalance()
    testLeftRightInBalance()
    testComplexLeftRightAndRightLeftTreeBalance()
    testRightInsertLoadTest()
    testLeftInsertLoadTest()

    # Test Deletion Balancing
    testBasicRootDeletion()
    testBasicLeftDeletion()
    testBasicRightDeletion()
    testRootRightReplacementDuringDeletion()
    testRootLeftReplacementDuringDeletion()
    testInorderDeleteLoadTest()
    testNonInorderDeleteLoadTest()
    testRootDeleteLoadTest()

    # Successor Tests
    testGetSuccessorRightWeighted()
    testGetSuccessorLeftWeighted()
    testGetSuccessorByKey()

    testGetNodesWithSmallerKeys()
    print("All tree tests passing!")


if __name__ == "__main__":
    runTests()
