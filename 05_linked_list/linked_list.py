from __future__ import annotations
from typing import Any, Optional


class Node(object):
    def __init__(self, data: Any, next_node: Node = None) -> None:
        self.data = data
        self.next = next_node


class LinkedList(object):
    def __init__(self, head=None) -> None:
        self.head = head

    def append(self, data: Any) -> None:
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert(self, data: Any) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def remove(self, data: Any) -> None:
        # import gc

        current_node = self.head
        # if head node' data is target data
        if current_node and current_node.data == data:
            self.head = current_node.next
            # gc.collect()
            current_node = None
            return
        # if next node's data is target data:
        prev_node = None
        while current_node and current_node.data != data:
            prev_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        prev_node.next = current_node.next
        # gc.collect()
        current_node = None

    def reverse_iterative(self) -> None:
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    def reverse_recursive(self) -> None:
        def _reverse_recursive(current_node: Node, prev_node: Node) -> Node:
            if current_node is None:
                return prev_node

            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
            return _reverse_recursive(current_node, prev_node)

        self.head = _reverse_recursive(self.head, None)

    def reverse_even(self) -> None:
        def _reverse_even(head: Node, prev_node: Node) -> Optional(Node):
            if head is None:
                return None

            current_node = head
            while current_node and current_node.data % 2 == 0:
                next_node = current_node.next
                current_node.next = prev_node
                prev_node = current_node
                current_node = next_node

            if current_node != head:  # current data is odd data or None
                head.next = current_node  # prev(even) -> ... -> head(even) -> current(odd or None)
                _reverse_even(current_node, None)
                return prev_node
            else:
                # for odd data
                head.next = _reverse_even(head.next, head)
                return head  # odd data

        self.head = _reverse_even(
            self.head, None
        )  # head -> ... -> prev head -> current(& next)


if __name__ == "__main__":
    l = LinkedList()
    l.append(1)
    l.append(2)
    l.append(4)
    l.append(6)
    l.append(1)
    l.append(3)
    l.append(5)
    l.append(2)
    l.append(4)
    l.append(6)
    l.print()
    print("######")
    l.reverse_even()
    l.print()
