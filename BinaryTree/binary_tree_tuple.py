class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


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

def display_keys(node, space = '\t', level=0):
    # if the node is empty
    if node is None:
        print(space*level + " ")
        return
    
    # if the node is leaf
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return
    
    #if the node has children
    display_keys(node.right, space, level+1)
    print(space*level + str(node.key))
    display_keys(node.left,space,level+1)

tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
tree1 = parse_tuple(tree_tuple)
display_keys(tree1)