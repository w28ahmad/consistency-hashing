from src.Tree import AVLTree, Node

def testFind():
    tree = AVLTree()
    assert tree.find(1) == None, "Find should return None for an empty tree"

    tree.insert(1)
    assert isinstance(tree.find(1), Node), "Find should return a Node for existing key"
    assert tree.find(1).key == 1, "Find should return the correct Node"

    assert tree.find(2) == None, "Find should return None for non-existing key"

def testInsert():
    tree = AVLTree()

    tree.insert(1)
    assert tree.root.key == 1, "Root key should be 1 after inserting 1"
    assert tree.root.height == 0, "Root height should be 0 after inserting 1"

    tree.insert(2)
    assert tree.root.right.key == 2, "The right child of root should have key 2 after inserting 2"
    assert tree.root.right.height == 0, "The right child of root should have height 1 after inserting 2"
    assert tree.root.height == 1, "Root height should be 1 after inserting 2"

def testIsHeightValid():
    tree = AVLTree()

    tree.insert(1)
    assert tree.isHeightValid(tree.root), "isHeightValid should return True after inserting 1"

    tree.insert(2)
    assert tree.isHeightValid(tree.root), "isHeightValid should return True after inserting 2"

def testIsBalanced():
    tree = AVLTree()

    tree.insert(1)
    assert tree.isBalanced(tree.root), "isBalanced should return True after inserting 1"

    tree.insert(2)
    assert tree.isBalanced(tree.root), "isBalanced should return True after inserting 2"

def testComplexBinaryTreeOperations():
    tree = AVLTree()

    # Insert values
    keysToInsert = [5, 2, 8, 1, 3, 7, 10, 4, 6, 9, 11]
    for key in keysToInsert:
        tree.insert(key)

    # Check the root
    assert tree.root.key == 5, "The root key should be 5"
    assert tree.root.height == 3, "The root height should be 4"

    # Check isHeightValid
    assert tree.isHeightValid(tree.root), "isHeightValid should return True"

    # Check isOrdered
    assert tree.isOrdered(tree.root), "isOrdered should return True"

    # Check find
    for key in keysToInsert:
        node = tree.find(key)
        assert isinstance(node, Node), f"Find should return a Node for existing key {key}"
        assert node.key == key, f"Find should return the correct Node for key {key}"

        # Check isBalanced - this test assumes that tree is properly balanced after inserts
        assert tree.isBalanced(node), "isBalanced should return True"

    # Check find for non-existent key
    assert tree.find(100) == None, "Find should return None for non-existing key 100"

    # The tree is valid AVLTree
    assert tree.isValid(tree.root), "The tree is left in a valid state"

def testBasicRightTreeInBalance():
    tree = AVLTree()

    keysToInsert = [1, 2, 3]

    for key in keysToInsert:
        tree.insert(key)

    assert tree.root.key == 2, "The root should have a value of 2 after balancing"
    assert tree.root.height == 1, "The root should have a height of 1 after balancing"
    assert tree.root.left.key == 1, "The left key is equal to 1"
    assert tree.root.right.key == 3, "The right key is equal to 3"
    assert tree.isValid(tree.root), "The tree is left in a valid state"

def testBasicLeftTreeInBalance():
    tree = AVLTree()

    keysToInsert = [3, 2, 1]

    for key in keysToInsert:
        tree.insert(key)

    assert tree.root.key == 2, "The root should have a value of 2 after balancing"
    assert tree.root.height == 1, "The root should have a height of 1 after balancing"
    assert tree.root.left.key == 1, "The left key is equal to 1"
    assert tree.root.right.key == 3, "The right key is equal to 3"
    assert tree.isValid(tree.root), "The tree is left in a valid state"

def testRightLeftInBalance():
    tree = AVLTree()

    keysToInsert = [1, 3, 2]

    for key in keysToInsert:
        tree.insert(key)

    assert tree.root.key == 2, "The root should have a value of 2 after balancing"
    assert tree.root.height == 1, "The root should have a height of 1 after balancing"
    assert tree.root.left.key == 1, "The left key is equal to 1"
    assert tree.root.right.key == 3, "The right key is equal to 3"
    assert tree.isValid(tree.root), "The tree is left in a valid state"

def testLeftRightInBalance():
    tree = AVLTree()

    keysToInsert = [3, 1, 2]

    for key in keysToInsert:
        tree.insert(key)

    assert tree.root.key == 2, "The root should have a value of 2 after balancing"
    assert tree.root.height == 1, "The root should have a height of 1 after balancing"
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
    assert tree.root.right.right.right.key == 40, "35's right child should be 40"

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

    assert tree.root == None, "Root is deleted and is None"

def testBasicLeftDeletion():
    tree = AVLTree()
    tree.insert(1)
    tree.insert(2)
    tree.delete(2)

    assert tree.root.key == 1, "Root remains 1"
    assert tree.root.left == None, "Root left is None"
    assert tree.root.right == None, "Root right is removed"
    assert tree.isValid(tree.root), "The tree is left in a valid state"

def testBasicRightDeletion():
    tree = AVLTree()
    tree.insert(2)
    tree.insert(1)
    tree.delete(1)

    assert tree.root.key == 2, "Root remains 2"
    assert tree.root.right == None, "Root right is None"
    assert tree.root.left == None, "Root left is Removed"
    assert tree.isValid(tree.root), "The tree is left in a valid state"

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

    print("All tests passed!")

if __name__ == "__main__":

    runTests()

