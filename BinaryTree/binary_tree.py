class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


node0 = TreeNode(3)
node1 = TreeNode(4)
node2 = TreeNode(5)
tree = node0 # root node 
print(node0.key)

node0.left = node1 # children of node0
node0.right = node2 # children of node0
