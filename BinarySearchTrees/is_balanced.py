import display as ds


class TreeNode():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def parse_tuple(data):
    if isinstance(data, tuple) and data == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])

    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node


def is_balanced(node):
    if node is None:
        return True, 0
    balanced_l, height_l = is_balanced(node.left)
    balanced_r, height_r = is_balanced(node.right)
    balanced = balanced_l and balanced_r and abs(height_l - height_r) <= 1
    height = 1 + max(height_l, height_r)
    return balanced, height


tree1 = parse_tuple((("aakash", "biraj", "hemanth"),
                    "jadesh", ("siddhant", "sonaksh", "vishal")))
ds.display_keys(tree1)
print(is_balanced(tree1))
