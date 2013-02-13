import pymongo
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet

class BrainMongo:
    def __init__(self, collection):
        self.collection = collection
    def insert(self, data):
        self.collection.insert(data)

    def activate(self):
        result = self.collection.find_one({"name":"buildNetwork"})
        print(self.collection)
        return result["activate"]

    def addSample(self, samples):
        raise NotImplementedError

    def SaveNetwork(self, network):
        raise NotImplementedError

    def insertvalue(self, key, value):
        return self.collection.insert({key:value, "C":"D"})

    def insertwithResult(self, key, result, value):
        output = self.collection.find_one(result)
        #Build network and insert results

class Network(object):
    """docstring for Network"""
    def __init__(self, *args,**kwargs):
        super(Network, self).__init__()
        self.network = buildNetwork(
            kwargs.get('input'),
            kwargs.get('hidden'),
            kwargs.get('output')
            )

        self.active = kwargs.get('activate')
        self.network.activate(self.active)