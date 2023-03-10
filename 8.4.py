class BinarySearchTree:
    class Node:
        def __init__(self, key, value, left=None, right=None):
            self.key = key
            self.value = value
            self.left = left
            self.right = right
            self.size = 1 + self.get_size(self.left) + self.get_size(self.right)
            self.height = 1 + max(self.get_height(self.left), self.get_height(self.right))

        def get_size(self, node):
            return 0 if node is None else node.size

        def get_height(self, node):
            return 0 if node is None else node.height

    def __init__(self):
        self.root = None

    def __len__(self):
        return self.size(self.root)

    def size(self, node):
        return 0 if node is None else node.size

    def height(self, node):
        return 0 if node is None else node.height

    def node_balance(self, node):
        return self.size(node.right) - self.size(node.left)

    def level_balance(self, node):
        return self.height(node.right) - self.height(node.left)

    def unbalanced_nodes(self, node=None, threshold=1):
        if node is None:
            node = self.root
        unbalanced = []
        if node is not None:
            if abs(self.node_balance(node)) > threshold or abs(self.level_balance(node)) > threshold:
                unbalanced.append(node.key)
            unbalanced.extend(self.unbalanced_nodes(node.left, threshold))
            unbalanced.extend(self.unbalanced_nodes(node.right, threshold))
        return unbalanced

    def insert(self, key, value):
        def do_insert(node):
            if node is None:
                return BinarySearchTree.Node(key, value)
            if key < node.key:
                node.left = do_insert(node.left)
            elif key > node.key:
                node.right = do_insert(node.right)
            else:
                node.value = value
            return node

        self.root = do_insert(self.root)

    def __str__(self):
        def do_str(node):
            if node is None:
                return ""
            return do_str(node.left) + str(node.key) + " " + do_str(node.right)

        return do_str(self.root)

# Example usage
bst = BinarySearchTree()
bst.insert(7, "A")
bst.insert(6, "B")
bst.insert(5, "C")
bst.insert(4, "D")
bst.insert(3, "E")
bst.insert(2, "F")
bst.insert(1, "G")
bst.insert(8, "H")
bst.insert(12, "I")
bst.insert(16, "J")
bst.insert(9, "K")
bst.insert(11, "L")
bst.insert(14, "M")
bst.insert(13, "N")
bst.insert(15, "O")

print(bst)
print("Node balance:", bst.node_balance(bst.root))
print("Level balance:", bst.level_balance(bst.root))
print("Unbalanced nodes (threshold=1):", bst.unbalanced_nodes(threshold=1))
print("Unbalanced nodes (threshold=2):", bst.unbalanced_nodes(threshold=2))

bst2 = BinarySearchTree()
bst2.insert(8, "A")
bst2.insert(4, "B")
bst2.insert(5, "C")
bst2.insert(6, "D")
bst2.insert(7, "E")
bst2.insert(3, "F")
bst2.insert(2, "G")
bst2.insert(1, "H")
bst2.insert(12, "I")
bst2
