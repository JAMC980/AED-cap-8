from binarytree import Node

def make_subtree(op, left, right):
    """Helper function to create a subtree with an operator as the root node."""
    root = Node(op)
    root.left = left
    root.right = right
    return root

def build_expression_tree(postfix):
    """Builds a binary tree to represent the given postfix expression."""
    stack = []
    for token in postfix.split():
        if token in "+-*/":
            right = stack.pop()
            left = stack.pop()
            stack.append(make_subtree(token, left, right))
        else:
            stack.append(Node(token))
    if len(stack) != 1:
        raise ValueError("Invalid postfix expression")
    return stack[0]

def inorder_traversal(root):
    """Returns the in-order traversal of the expression tree as a string."""
    if root is None:
        return ""
    if root.left is None and root.right is None:
        return str(root.value)
    left = "(" + inorder_traversal(root.left) + ")" if root.left is not None else ""
    right = "(" + inorder_traversal(root.right) + ")" if root.right is not None else ""
    return left + str(root.value) + right

def preorder_traversal(root):
    """Returns the pre-order traversal of the expression tree as a string."""
    if root is None:
        return ""
    if root.left is None and root.right is None:
        return str(root.value)
    left = preorder_traversal(root.left)
    right = preorder_traversal(root.right)
    return str(root.value) + left + right

def postorder_traversal(root):
    """Returns the post-order traversal of the expression tree as a string."""
    if root is None:
        return ""
    if root.left is None and root.right is None:
        return str(root.value)
    left = postorder_traversal(root.left)
    right = postorder_traversal(root.right)
    return left + right + str(root.value)

# Example usage
expressions = [
    "a 9 1 5 + 1 5 + 1 9 + 4 * +",
    "b B * A C 4 ** -",
    "c 4 2",
    "d A 5 7 +",
    "e + /"
]

for expr in expressions:
    try:
        tree = build_expression_tree(expr)
        print(f"In-order: {inorder_traversal(tree)}")
        print(f"Pre-order: {preorder_traversal(tree)}")
        print(f"Post-order: {postorder_traversal(tree)}")
    except ValueError as e:
        print(f"Error: {str(e)}")



