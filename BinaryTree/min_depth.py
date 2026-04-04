class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def minDepth(root):
        if root is None:
            return 0
        if root.left is None:
            return 1 + minDepth(root.right)
        if root.right is None:
            return 1 + minDepth(root.left)
        return 1 + min(minDepth(root.left), minDepth(root.right))

def parse_tuple(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])

    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node

tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
tree1 = parse_tuple(tree_tuple)
solution = minDepth(tree1)
print(solution)