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


tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
tree1 = parse_tuple(tree_tuple)
print(f"                  {tree1.key}")  # should print 2
print(f"            {tree1.left.key}            {tree1.right.key}")
print(f"     {tree1.left.left.key}          {tree1.left.right} {tree1.right.left.key}        {tree1.right.right.key}")
print(
    f"                        {tree1.right.left.right.key}  {tree1.right.right.left.key}     {tree1.right.right.right.key}")
