
class BSTNode:
    '''
    Class to represent a single Binary Search Tree Node;
    Has parent, left, and right nodes
    '''
    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None


class BST:
    '''
    Class to represent an entire Binary Search Tree with
    multiple nodes
    '''
    def __init__(self):
        self.root = None