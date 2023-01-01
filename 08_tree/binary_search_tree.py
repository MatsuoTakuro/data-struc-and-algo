from typing import Any


class Node(object):
    def __init__(self, value: Any) -> None:
        self.value = value
        self.left = None
        self.right = None


def insert(node: Node, value: Any) -> Node:
    if node is None:
        return Node(value)

    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    return node


if __name__ == "__main__":
    root = insert(None, 3)
    root = insert(root, 6)
    root = insert(root, 5)
    root = insert(root, 7)
    root = insert(root, 1)
    root = insert(root, 10)
    root = insert(root, 2)
    print(root.left.right.value)
