from collections import Counter
import heapq
from typing import List


def top_n_with_heap(words: list[str], n: int) -> list[str]:
    # d = {}
    # for word in words:
    #     d[word] = d.get(word, 0) + 1
    # data = [(-d[word], word) for word in d]
    # heapq.heapify(data)
    # return [heapq.heappop(data)[1] for _ in range(n)]

    counter_words = Counter(words)
    # return [word[0] for word in counter_words.most_common(n)]

    data = [(-counter_words[word], word) for word in counter_words]
    heapq.heapify(data)
    return [heapq.heappop(data)[1] for _ in range(n)]


if __name__ == "__main__":
    w = ["python", "c", "java", "go", "python", "c", "go", "python"]
    print(top_n_with_heap(w, 3))
