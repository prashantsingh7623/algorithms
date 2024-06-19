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

def iterative_inorder_traversal(root: Node):
    if root is None:
        return
    
    s = [root]
    res = []
    while len(s) > 0:
        node = s[-1]
        if node.left is not None:
            s.append(node.left)
        else:
            while len(s) > 0:
                node = s.pop()
                res.append(node.value)
                if node.right is not None:
                    s.append(node.right)
                    break

    return res

def recursiveInOrderTraversal(root: Node):
    if root is None:
        return
    
    recursiveInOrderTraversal(root=root.left)
    print(root.value)
    recursiveInOrderTraversal(root=root.right)

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

def recursivePreOrderTraversal(root):
    if root is None:
        return
    print(root.value)
    recursivePreOrderTraversal(root=root.left)
    recursivePreOrderTraversal(root=root.right)

def levelOrderTraversal(root):
    if root is None:
        return
    
    q = [root]
    result = []
    while len(q) > 0:
        node = q.pop(0)
        result.append(node.value)
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)
    return result

def levelOrderTraversalList(root: Node) -> list:
    if root is None:
        return
    
    q = [root,None]
    res = [[root.value]]
    while len(q) > 0:
        node = q.pop(0)
        if len(q) == 0:
            break
        if node is None:
            res.append([i.value for i in q])
            q.append(None)
        else:
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)

    return res

# print(iterative_preorder_traversal(root=root))
# print(levelOrderTraversalList(root=root))
# recursivePreOrderTraversal(root)
# recursiveInOrderTraversal(root)
print(iterative_inorder_traversal(root=root))
