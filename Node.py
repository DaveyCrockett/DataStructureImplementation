class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

    def insert(self, root, key):
        if root is None:
            return Node(key)
        else:
            if root.value == key:
                return root
            elif root.value < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
            return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.value)
            self.inorder(root.right)

