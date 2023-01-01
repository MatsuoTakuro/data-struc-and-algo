from typing import Any


class Node(object):
    def __init__(self, value: Any) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self) -> None:
        self.root = None

    def insert(self, value: Any) -> Node:
        if self.root is None:
            self.root = Node(value)
            return

        def _insert(node: Node, value: Any) -> Node:
            if node is None:
                return Node(value)

            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node

        _insert(self.root, value)

    # in_order:   left -> root  -> right
    # pre_order:  root -> left  -> right
    # post_order: left -> right -> root
    def in_order(self) -> None:
        def _in_order(node: Node) -> None:
            if node is not None:
                _in_order(node.left)

                print(node.value)
                _in_order(node.right)

        _in_order(self.root)

    def search(self, value: Any) -> bool:
        def _search(node: Node, value: Any) -> bool:
            if node is None:
                return False

            if value < node.value:
                return _search(node.left, value)

            if value == node.value:
                return True

            if node.value < value:
                return _search(node.right, value)

        return _search(self.root, value)

    def min_node(self, node: Node) -> Node:
        current = node
        while current.left:
            current = current.left
        return current

    def remove(self, value: Any) -> Node:
        def _remove(node: Node, value: Any) -> Node:
            if node is None:
                return node

            if value < node.value:
                node.left = _remove(node.left, value)
            elif value > node.value:
                node.right = _remove(node.right, value)
            else:  # value == node.value
                if node.left is None:
                    return node.right

                if node.right is None:
                    return node.left

                temp_node = self.min_node(node.right)
                node.value = temp_node.value
                node.right = _remove(node.right, temp_node.value)

            return node

        return _remove(self.root, value)


if __name__ == "__main__":
    # result after remove(root, 6)
    #     3                 3
    #    / \               / \
    #   /   \             /   \
    #  1     6      ->   1     7
    #   \   / \           \   / \
    #    2 5   9           2 5   9
    #         / \               / \
    #        8   10            8   10
    #       /
    #      7

    bst = BinarySearchTree()
    bst.insert(3)
    bst.insert(6)
    bst.insert(5)
    bst.insert(9)
    bst.insert(1)
    bst.insert(10)
    bst.insert(2)
    bst.insert(8)
    bst.insert(7)
    bst.in_order()
    print("####### Search")
    print(bst.search(2))
    print(bst.search(5))
    print(bst.search(4))
    print("####### Remove")
    bst.remove(6)
    bst.in_order()
