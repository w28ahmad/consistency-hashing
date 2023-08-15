from src.Tree import AVLTree
from hashlib import sha256


class HashRing:
    def __init__(self):
        self.hashring = AVLTree()

    def hash(self, key):
        hash = sha256(key.encode())
        return int(hash.hexdigest(), 16)

    def insert(self, key, data):
        pass


