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


# in_order: left -> root -> right
# pre_order: root -> left -> right
# post_order: left -> right -> root
def in_order(node: Node) -> None:
    if node is not None:
        in_order(node.left)

        print(node.value)
        in_order(node.right)


def search(node: Node, value: Any) -> bool:
    if node is None:
        return False

    if value < node.value:
        return search(node.left, value)

    if value == node.value:
        return True

    if node.value < value:
        return search(node.right, value)


if __name__ == "__main__":
    root = insert(None, 3)
    root = insert(root, 6)
    root = insert(root, 5)
    root = insert(root, 7)
    root = insert(root, 1)
    root = insert(root, 10)
    root = insert(root, 2)
    in_order(root)
    print(search(root, 2))
    print(search(root, 5))
    print(search(root, 4))
