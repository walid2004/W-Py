#Data structure manipulation, turning a python list into a binary tree
class BinaryTree:
    class Node:
        def __init__(self,item):
            pass
        pass
    def __init__(self,dataList):
        self.size = len(dataList)
        self.data= sorted(dataList)
        self.root= None
        pass