from src.Tree import AVLTree
from hashlib import sha256


class HashRing:
    def __init__(self):
        self.hashring = AVLTree()

    '''
    @param id: String
    @returns Int
    '''

    def hashInt(self, id):
        hash = sha256(id.encode())
        return int(hash.hexdigest(), 16)

    '''
    @param nodeId: String
    @returns Node
    '''

    def putNode(self, nodeId):
        # Get hashInt
        key = self.hashInt(nodeId)

        # Add the node to the AVLTree
        # The data data stucture is also an AVLtree
        node = self.hashring.insert(key, AVLTree())

        # Get the successor
        successor = self.hashring.getSuccessorByNode(node)

        # If no successor, the successor is the
        # first node in the hashring
        if successor is None:
            successor = self.hashring.getSmallestNode()

        # This is not the only added node
        if successor.key != key:
            # Move the data from successor which
            # belongs to the current node
            nodeDataTree = node.data
            successorDataTree = successor.data

            # The data that needs to move
            # are the keys which fall before
            # equal to the current keys value
            nodesToMove = successorDataTree.getNodesWithSmallerKeys(key)

            for node in nodesToMove:
                nodeDataTree.insert(node.key, node.data)
                successorDataTree.delete(node.key)

    '''
    @param nodeId: String
    @returns None
    '''

    def removeNode(self, nodeId):
        # Get hashInt
        key = self.hashInt(nodeId)

        # Get the node
        node = self.hashring.find(key)

        # Get the successor
        successor = self.hashring.getSuccessorByNode(node)

        # If no successor, the successor is the
        # first node in the hashring
        if successor is None:
            successor = self.hashring.getSmallestNode()

        # We have not removed all servers
        if successor.key != key:
            # Move the data
            nodeDataTree = node.data
            successorDataTree = successor.data

            while not nodeDataTree.isEmpty():
                dataKey, data = nodeDataTree.root.key, nodeDataTree.root.data
                successorDataTree.insert(dataKey, data)
                nodeDataTree.delete(nodeDataTree.root.key)

        # delete node
        self.hashring.delete(key)

    '''
    @param id: String
    @returns None
    '''

    def putData(self, id, data):
        # Find the hashInt
        key = self.hashInt(id)

        # Find the node where data needs to go
        successor = self.hashring.getSuccessorByKey(key)
        if successor is None:
            successor = self.hashring.getSmallestNode()
        if successor is None:
            print("No Storage Nodes")
            return

        # Add the data to the node
        successorDataTree = successor.data
        successorDataTree.insert(key, data)

    '''
    @param id: String
    @returns None
    '''

    def getData(self, id):
        # Find hashInt
        key = self.hashInt(id)

        # Find the node where the data should exist
        successor = self.hashring.getSuccessorByKey(key)
        if successor is None:
            successor = self.hashring.getSmallestNode()
        if successor is None:
            print("No Storage Node")
            return

        # Get the data from the node
        successorDataTree = successor.data
        return successorDataTree.find(key).data

    '''
    @param id: String
    @returns None
    '''

    def removeData(self, id):
        # Get hashInt
        key = self.hashInt(id)

        # Find the node where data exists
        successor = self.hashring.getSuccessorByKey(key)
        if successor is None:
            successor = self.hashring.getSmallestNode()
        if successor is None:
            print("No Storage Node")
            return

        # Remove the data from the node
        successorDataTree = successor.data
        successorDataTree.delete(key)
