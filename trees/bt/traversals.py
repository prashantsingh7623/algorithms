class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

root = Node(1)
root.left  = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)

def iterative_preorder_traversal(root: Node):
    if root is None:
        return
    
    values = []
    LAST_VISITED = [root]
    while len(LAST_VISITED) > 0:
        root = LAST_VISITED.pop()
        values.append(root.value)

        if root.right is not None:
            LAST_VISITED.append(root.right)
        if root.left is not None:
            LAST_VISITED.append(root.left)

    return values

print(iterative_preorder_traversal(root=root))

