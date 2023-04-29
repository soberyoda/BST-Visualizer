# klasa Node - reprezentująca węzeł drzewa BST

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# klasa BST - reprezentacja całego drzewa
class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.search(value) is not None:
            return  # wartość już występuje w drzewie
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(value, node.left)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(value, node.right)

    def delete(self, value):
        self.root = self._delete(value, self.root)

    def _delete(self, value, node):
        if node is None:
            return node
        if value < node.value:
            node.left = self._delete(value, node.left)
        elif value > node.value:
            node.right = self._delete(value, node.right)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            temp = self._minValueNode(node.right)
            node.value = temp.value
            node.right = self._delete(temp.value, node.right)
        return node

    def _minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, node):
        if node is None or node.value == value:
            return node

        if node.value < value:
            return self._search(value, node.right)

        return self._search(value, node.left)


