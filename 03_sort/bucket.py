from typing import List


def insertion_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(1, len_numbers):
        right_temp = numbers[i]
        left_idx = i - 1
        while left_idx >= 0 and numbers[left_idx] > right_temp:
            numbers[left_idx + 1] = numbers[left_idx]
            left_idx -= 1
        numbers[left_idx + 1] = right_temp
    return numbers


def bucket_sort(numbers: List[int]) -> List[int]:
    max_num = max(numbers)
    len_numbers = len(numbers)
    size = max_num // len_numbers

    buckets = [[] for _ in range(size)]
    for num in numbers:
        i = num // size
        if i != size:
            buckets[i].append(num)
        else:
            buckets[size - 1].append(num)
    print(buckets)

    for i in range(size):
        insertion_sort(buckets[i])
    print(buckets)

    result = []
    for i in range(size):
        result += buckets[i]

    return result


if __name__ == "__main__":
    import random

    nums = [random.randint(0, 1000) for _ in range(10)]
    print(bucket_sort(nums))
