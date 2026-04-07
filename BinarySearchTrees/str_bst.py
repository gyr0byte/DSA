class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def parse_tuple_to_bst(data):
    if not data:
        return None

    key, left_data, right_data = data
    node = TreeNode(key)
    node.left = parse_tuple_to_bst(left_data)
    node.right = parse_tuple_to_bst(right_data)

    return node
