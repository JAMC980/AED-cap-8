class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, key, value):
        new_node = Node(key, value)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while current:
                if key == current.key:
                    while current.left is not None:
                        current = current.left
                    current.left = new_node
                    return
                elif key < current.key:
                    if current.left is None:
                        current.left = new_node
                        return
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        return
                    else:
                        current = current.right
    
    def find(self, key, shallowest=False):
        current = self.root
        result = None
        while current:
            if current.key == key:
                if shallowest:
                    result = current
                    current = current.left
                else:
                    result = current
                    current = current.right
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return result
    
    def delete(self, key, shallowest=False):
        parent = None
        current = self.root
        while current:
            if current.key == key:
                if current.left is None and current.right is None:
                    if parent is None:
                        self.root = None
                    elif parent.left == current:
                        parent.left = None
                    else:
                        parent.right = None
                elif current.left is None:
                    if parent is None:
                        self.root = current.right
                    elif parent.left == current:
                        parent.left = current.right
                    else:
                        parent.right = current.right
                elif current.right is None:
                    if parent is None:
                        self.root = current.left
                    elif parent.left == current:
                        parent.left = current.left
                    else:
                        parent.right = current.left
                else:
                    successor = current.left
                    while successor.right:
                        successor = successor.right
                    current.key = successor.key
                    current.value = successor.value
                    if shallowest:
                        self.delete(successor.key, shallowest=True)
                    else:
                        self.delete(successor.key)
                return
            elif key < current.key:
                parent = current
                current = current.left
            else:
                parent = current
                current = current.right
