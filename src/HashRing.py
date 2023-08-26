from src.Tree import AVLTree
from hashlib import sha256

debug = False


class HashRing:
    def __init__(self):
        self.hashring = AVLTree()
        self.keyToId = {}

    '''
    @param id: String
    @returns Int
    '''

    def hashInt(self, id):
        hash = sha256(id.encode())
        key = int(hash.hexdigest(), 16)
        if debug:
            self.keyToId[key] = id
        return key

    '''
    @param nodeId: String
    @returns Node
    '''

    def putNode(self, nodeId):
        # Get hashInt
        key = self.hashInt(nodeId)

        # Add the node to the AVLTree
        # The data data stucture is also an AVLtree
        self.hashring.insert(key, AVLTree())
        node = self.hashring.find(key)

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
            if self.hashring.isSmallestNode(key):
                # Need to transfer the loop over nodes
                nodesToMove.extend(successorDataTree
                    .getNodesWithInvalidKeys(successor.key))

            for node in nodesToMove:
                if debug:
                    print(f"moving node with key {node.data} \
                            to {nodeId} from {self.keyToId[successor.key]}")
                nodeDataTree.insert(node.key, node.data)
                successorDataTree.delete(node.key)

    '''
    @param nodeId: String
    @returns None
    '''

    def removeNode(self, nodeId):
        # Get hashInt
        removalKey = self.hashInt(nodeId)

        # Get the node
        node = self.hashring.find(removalKey)

        # Get the successor
        successor = self.hashring.getSuccessorByNode(node)

        # Get smallest node incase
        # we need to loop nodes around to the Start
        smallestNode = self.hashring.getSmallestNode()

        # If no successor, the successor is the
        # first node in the hashring
        if successor is None:
            successor = self.hashring.getSmallestNode()
        if successor is None:
            print("All Nodes Cleared -- Dropping Remaining Data")
            return

        # We have not removed all servers
        if successor.key != removalKey:
            # Move the data
            nodeDataTree = node.data
            successorDataTree = successor.data
            smallestNodeDataTree = smallestNode.data

            while not nodeDataTree.isEmpty():
                dataKey, data = nodeDataTree.root.key, nodeDataTree.root.data
                if debug:
                    print(f"Trying to remove {data}")
                if dataKey > removalKey and smallestNode.key != removalKey:
                    # Loop around
                    smallestNodeDataTree.insert(dataKey, data)
                else:
                    successorDataTree.insert(dataKey, data)
                nodeDataTree.delete(nodeDataTree.root.key)

        # delete node
        self.hashring.delete(removalKey)

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

        if debug:
            print(f"Adding data {data} to {self.keyToId[successor.key]}")

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

    def printDebug(self):
        print(self.keyToId)
