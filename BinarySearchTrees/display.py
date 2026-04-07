def display_keys(node, space = '\t', level=0):
    # if the node is empty
    if node is None:
        print(space*level + "None")
        return
    
    # if the node is leaf
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return
    
    #if the node has children
    display_keys(node.right, space, level+1)
    print(space*level + str(node.key))
    display_keys(node.left,space,level+1)
