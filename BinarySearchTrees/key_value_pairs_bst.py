import display as ds


class BSTNode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class User:
    def __init__(self, username):
        self.username = username


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


def insert(node, key, value):
    if node is None:
        node = BSTNode(key, value)
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node


tree1 = parse_tuple((("aakash", "biraj", "hemanth"),
                    "jadhesh", ("siddhant", "sonaksh", "vishal")))
jadhesh = User("jadhesh")
tree = BSTNode(jadhesh.username, jadhesh)
insert(tree1, "Tanya", User("Tanya"))

ds.display_keys(tree1)
