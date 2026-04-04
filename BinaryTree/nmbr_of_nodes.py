class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)
    
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
number_of_nodes = tree_size(tree1)

print(number_of_nodes)