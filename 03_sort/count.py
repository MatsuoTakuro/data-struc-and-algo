from typing import List


def counting_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    max_num = max(numbers)
    counts = [0] * (max_num + 1)
    result = [0] * len_numbers

    for num in numbers:
        counts[num] += 1

    for counts_idx in range(1, len(counts)):
        counts[counts_idx] += counts[counts_idx - 1]

    number_idx = len_numbers - 1
    while number_idx >= 0:
        counts_idx = numbers[number_idx]
        result[counts[counts_idx] - 1] = numbers[number_idx]
        counts[counts_idx] -= 1
        number_idx -= 1

    return result


if __name__ == "__main__":
    import random

    nums = [random.randint(0, 1000) for _ in range(10)]
    # nums = [4, 3, 6, 2, 3, 4, 7]
    print(counting_sort(nums))
