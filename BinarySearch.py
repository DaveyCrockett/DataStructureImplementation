class BinarySearch:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def search(self, root, key):
        if root is None or root.value == key:
            return root
        if root.value < key:
            return self.search(root.right, key)
        return self.search(root.left, key)

    def insert(self, root, key):
        if root is None:
            return BinarySearch(key)
        else:
            if root.val == key:
                return root
            elif root.val < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root