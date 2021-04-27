class BinarySearch:
    def __init__(self):
        pass

    def search(self, root, key):
        if root is None or root.value == key:
            return root
        if root.value < key:
            return self.search(root.right, key)
        return self.search(root.left, key)