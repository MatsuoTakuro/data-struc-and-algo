from typing import Any


class Stack(object):
    def __init__(self) -> None:
        self.stack = []  # Python List is stack

    def push(self, data) -> None:
        self.stack.append(data)

    def pop(self) -> Any:
        if self.stack:
            return self.stack.pop()


if __name__ == "__main__":
    s = Stack()
    print(s.stack)
    s.push(1)
    print(s.stack)
    s.push(2)
    print(s.stack)
    print(s.pop())
    print(s.stack)
    print(s.pop())
    print(s.stack)
