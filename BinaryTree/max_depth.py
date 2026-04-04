class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def maxDepth(self, root):
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))