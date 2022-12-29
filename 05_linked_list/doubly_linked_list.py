from __future__ import annotations
from typing import Any, Optional


class Node(object):
    def __init__(
        self, data: Any, next_node: Node = None, prev_node: Node = None
    ) -> None:
        self.data = data
        self.next = next_node
        self.prev = prev_node


class DoublyLinkedList(object):
    def __init__(self, head: Node = None) -> None:
        self.head = head

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node

    def insert(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def print(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def remove(self, data: Any) -> Optional[Node]:
        current_node = self.head
        if current_node and current_node.data == data:
            # head node containing target data, followed by none
            if current_node.next is None:
                current_node = None
                self.head = None
                return None
            # head node containing target data, followed by one or more nodes
            else:
                next_node = current_node.next
                next_node.prev = None
                current_node = None
                self.head = next_node
                return self.head

        while current_node and current_node.data != data:
            current_node = current_node.next

        # no node containing targe data
        if current_node is None:
            return None

        # last node containig target data
        if current_node.next is None:
            prev_node = current_node.prev
            prev_node.next = None
            current_node = None
            return self.head
        # middle node containig target data
        else:
            next_node = current_node.next
            prev_node = current_node.prev
            prev_node.next = next_node
            next_node.prev = prev_node
            current_node = None
            return self.head

    # init  : none <- 1 <-> 2 <-> 3 -> none
    # loop 0:               2 <-  1 -> none
    # loop 1:         3 <-  2 <-> 1 -> none
    # loop 2: none <- 3 <-> 2 <-> 1 -> none
    def reverse_iterative(self) -> None:
        prev_node = None
        current_node = self.head
        while current_node:
            prev_node = current_node.prev
            current_node.prev = current_node.next
            current_node.next = prev_node

            current_node = current_node.prev

        if prev_node:  # prev_node.data = 2
            self.head = prev_node.prev  # prev_node.prev.data = 3

    def reverse_recursive(self) -> None:
        # init  : none <- 3 <-> 2 <-> 1 -> none
        # loop 0:               2 <-  3 -> none
        # loop 1:         1 <-  2 <-> 3 -> none
        # loop 2: none <- 1 <-> 2 <-> 3 -> none
        def _reverse_recursive(current_node: Node) -> Optional[Node]:
            if current_node is None:
                return None

            prev_node = current_node.prev
            current_node.prev = current_node.next
            current_node.next = prev_node

            if current_node.prev is None:
                return current_node

            return _reverse_recursive(current_node.prev)

        self.head = _reverse_recursive(self.head)

    def sort(self) -> None:
        if self.head is None:
            return

        current_node = self.head
        while current_node.next:
            next_node = current_node.next
            while next_node:
                if current_node.data > next_node.data:
                    current_node.data, next_node.data = (
                        next_node.data,
                        current_node.data,
                    )
                next_node = next_node.next
            current_node = current_node.next


if __name__ == "__main__":
    d = DoublyLinkedList()
    d.append(1)
    d.append(5)
    d.append(2)
    d.append(9)
    d.print()
    print("######## Sort")
    d.sort()
    d.print()
