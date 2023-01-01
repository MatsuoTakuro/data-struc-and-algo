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


def min_node(node: Node) -> Node:
    current = node
    while current.left:
        current = current.left
    return current


def remove(node: Node, value: Any) -> Node:
    if node is None:
        return node

    if value < node.value:
        node.left = remove(node.left, value)
    elif value > node.value:
        node.right = remove(node.right, value)
    else:  # value == node.value
        if node.left is None:
            return node.right

        if node.right is None:
            return node.left

        temp_node = min_node(node.right)
        node.value = temp_node.value
        node.right = remove(node.right, temp_node.value)

    return node


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
    root = insert(None, 3)
    root = insert(root, 6)
    root = insert(root, 5)
    root = insert(root, 9)
    root = insert(root, 1)
    root = insert(root, 10)
    root = insert(root, 2)
    root = insert(root, 8)
    root = insert(root, 7)
    in_order(root)
    print(search(root, 2))
    print(search(root, 5))
    print(search(root, 4))
    print("####### Remove")
    in_order(remove(root, 6))
