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
        self.hashring.insert(key)

        # Move data from next node that
        # Belongs in this node
        # TODO
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

        # Move the data

        # Remove node
        self.hashring.remove(key)

        pass

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
