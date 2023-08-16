from src.Tree import AVLTree
from hashlib import sha256


class HashRing:
    def __init__(self):
        self.hashring = AVLTree()

    '''
    @param key: String
    @returns Int
    '''

    def hashInt(self, key):
        hash = sha256(key.encode())
        return int(hash.hexdigest(), 16)

    '''
    @param nodeId: String
    @returns Node
    '''

    def addNode(self, nodeId):
        # Get hashInt

        # Add the node to the AVLTree

        # Move data from next node that
        # Belongs in this node

        pass

    '''
    @param nodeId: String
    @returns None
    '''

    def removeNode(self, nodeId):
        # Get hashInt

        # Get the node

        # Move the data out to next node on ring

        # Remove node

        pass

    '''
    @param key: String
    @returns None
    '''

    def addData(self, key, data):
        # Find the hashInt

        # Find the node where data needs to go

        # Add the data to the node
        pass

    '''
    @param key: String
    @returns None
    '''

    def getData(self, key):
        # Find hashInt

        # Find the node where the data should exist

        # Get the data from the node
        pass
