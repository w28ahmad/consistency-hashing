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
        pass

    '''
    @param nodeId: String
    @returns None
    '''

    def removeNode(self, nodeId):
        pass

    '''
    @param key: String
    @returns None
    '''

    def addData(self, key, data):
        pass

    '''
    @param key: String
    @returns None
    '''

    def getData(self, key):
        pass
