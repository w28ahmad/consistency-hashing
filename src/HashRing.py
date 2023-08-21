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
        successor = self.hashring.getSuccessor(node)

        # If no successor, the successor is the
        # first node in the hashring
        if successor is None:
            successor = self.hashring.getSmallestNode()

        # This is not the only added node
        if successor.key != key:
            # Move the data from successor which
            # belongs to the current node
            nodeData = node.data
            successorData = successor.data

            # The data that needs to move
            # are the keys which fall before 
            # equal to the current keys value

            pass

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
        successor = self.hashring.getSuccessor(node)

        # If no successor, the successor is the
        # first node in the hashring
        if successor is None:
            successor = self.hashring.getSmallestNode()

        # We have not removed all servers
        if successor.key != key:
            # Move the data
            nodeData = node.data
            successorData = successor.data

            while not nodeData.isEmpty():
                dataKey, data = nodeData.root.key, nodeData.root.data
                successorData.insert(dataKey, data)
                nodeData.delete(nodeData.root.key)

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

        # Add the data to the node
        pass

    '''
    @param id: String
    @returns None
    '''

    def getData(self, id):
        # Find hashInt
        key = self.hashInt(id)

        # Find the node where the data should exist

        # Get the data from the node
        pass

    '''
    @param id: String
    @returns None
    '''

    def removedata(self, id):
        # Get hashInt
        key = self.hashInt(id)

        pass
