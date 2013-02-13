import brainmongo
import unittest

class TestStart(unittest.TestCase):
    """docstring for TestStart"""
    def __init__(self, arg):
        client = MongoClient()
        db = client.mlbase
        db = client["mlbase"]
        collection =db.mlbase

        b = BrainMongo(collection)
        net = buildNetwork(2,4,1)
        net.activate(b.activate())
        print(b.activate())
