import display as ds

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


def is_bst(node, left=None, right=None):
    if not node:
        return True

    if left is not None and node.key <= left:
        return False
    if right is not None and node.key >= right:
        return False
    return (is_bst(node.left, left, node.key) and is_bst(node.right, node.key, right))


tree1 = parse_tuple((("aakash", "biraj", "hemanth"),
                    "jadesh", ("siddhant", "sonaksh", "vishal")))
result = is_bst(tree1)
ds.display_keys(tree1)
print(result)
