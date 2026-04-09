
class Treenode:
    """
        create tree manually
    """
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# node0 = Treenode(5)
# node1 = Treenode(3)
# node2 = Treenode(4)  
# node3 = Treenode(6)
# node4 = Treenode(2)      
# node0.left = node1
# node0.right = node2
# tree = node0
# print(tree.left.key)
# print(tree.key)
# print(tree.right.key)
# node0.left.left = node4
# node0.right.right = node3
# print(node0.left.left.key)
# print(Treenode.__doc__)

tree_tuple = ((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8)))

def parse_tuple(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = Treenode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = Treenode(data)
    return node

tree = parse_tuple(((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8))))
print(tree.key)
print(tree.left.key)

def display_keys(node, space='\t', level=0):
    # print(node.key if node else None, level)
    
    # If the node is empty
    if node is None:
        print(space*level + '∅')
        return   
    
    # If the node is a leaf 
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return
    
    # If the node has children
    display_keys(node.right, space, level+1)
    print(space*level + str(node.key))
    display_keys(node.left,space, level+1)

    print(display_keys(tree, " "))    