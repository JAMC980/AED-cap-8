class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def build_tree_from_array(arr):
    n = len(arr)
    nodes = [None]*n
    for i in range(n-1, -1, -1):
        if arr[i] != "none":
            nodes[i] = Node(arr[i])
            if 2*i+1 < n:
                nodes[i].left = nodes[2*i+1]
            if 2*i+2 < n:
                nodes[i].right = nodes[2*i+2]
    root = nodes[0]
    if root is None:
        raise Exception("Cannot build tree")
    return root

# array 1
arr1 = [3, 2, 4, "none", "none", "none", 6]
root1 = build_tree_from_array(arr1)
# print tree in inorder traversal
def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.key)
    inorder(node.right)
inorder(root1)

# array 2
arr2 = [55, 12, 71, "none", 4, "none", "none"]
root2 = build_tree_from_array(arr2)
inorder(root2)

# array 3
arr3 = [55, 12, "none", 4]
try:
    root3 = build_tree_from_array(arr3)
except Exception as e:
    print(e)

# array 4
arr4 = [55, 12, "none", 4, "none", "none", 65, 97, 8,  "none", "none", "none", "none", "none", "none", "none", "none", 6, "none"]
root4 = build_tree_from_array(arr4)
inorder(root4)

# array 5
arr5 = [55, 12, "none", "none", 65, "none", 4, "none", 8, "none", "none", "none", "none", "none", "none", "none", "none", 6, "none"]
try:
    root5 = build_tree_from_array(arr5)
except Exception as e:
    print(e)
