from collections import deque
from typing import Any


class Queue(object):
    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, data: Any) -> None:
        self.queue.append(data)

    def dequeue(self) -> Any:
        if self.queue:
            return self.queue.pop(0)


def reverse(queue: deque) -> deque:
    new_queue = deque()
    while queue:
        new_queue.append(queue.pop())  # deque.pop() like stack
    [queue.append(d) for d in new_queue]


if __name__ == "__main__":
    print("###### Queue")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.queue)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.queue)

    print("###### Deque")
    q2 = deque()
    q2.append(1)
    q2.append(2)
    q2.append(3)
    q2.append(4)
    print(q2)
    print(q2.popleft())
    print(q2.popleft())
    print(q2.popleft())
    print(q2.popleft())
    print(q2)

    print("###### Deque Reverse")
    q3 = deque()
    q3.append(1)
    q3.append(2)
    q3.append(3)
    q3.append(4)
    print(q3)
    # q3.reverse()
    reverse(q3)
    print(q3)
