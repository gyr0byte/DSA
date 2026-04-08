class BSTNode():
    def __init__(self, key, value = None):
        self.ley = key
        self.vlaue = value
        self.left = None
        self.right = None
        self.parent = None
        
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

tree1 = parse_tuple((("aakash", "biraj", "hemanth"), "jadhesh", ("siddhant", "sonaksh", "vishal")))
tree = BSTNode(jadhesh.username, jadhesh)
print(tree.key)