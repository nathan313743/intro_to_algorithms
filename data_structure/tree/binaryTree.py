class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = 0

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def find_min_recursive(self, root):
        if root is None:
            return -1
        if root.left is None:
            return root.data
        return self.find_min_recursive(root.left)

    def find_min(self):
        return self.find_min_recursive(self.root)

    def search_recursive(self, root, data):
        if root is None:
            return False
        if data == root.data:
            return True
        elif data < root.data:
            return self.search_recursive(root.left, data)
        return self.search_recursive(root.right, data)

    def search(self, data):
        return self.search_recursive(self.root, data)

    def insert_recursive(self, root, data):
        if root is None:
            new_node = Node()
            new_node.data = data
            return new_node

        if  data <= root.data:
            root.left = self.insert_recursive(root.left, data)
        elif data > root.data:
            root.right = self.insert_recursive(root.right, data)
        return root

    def find_height_recursive(self, root):
        if root is None:
            return -1

        result1 = self.find_height_recursive(root.left)
        result2 = self.find_height_recursive(root.right)
        return max(result1, result2)  + 1

    def find_height(self):
        return self.find_height_recursive(self.root)

    def insert(self, data):
        self.root = self.insert_recursive(self.root, data)

if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.insert(3)
    tree.insert(2)
    tree.find_height()
    tree.insert(10)
    tree.insert(20)
    tree.insert(30)
    tree.insert(9)
    tree.insert(16)
    tree.insert(17)
    result = tree.search(10)
    print(result)
    result = tree.search(30)
    print(result)
    result = tree.search(16)
    print(result)
    result = tree.search(5)
    print(result)
    result = tree.search(345)
    print(result)
    print("Min value is: " + str(tree.find_min()))
    print("Max height = " + str(tree.find_height()))
