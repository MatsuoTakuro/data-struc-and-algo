from typing import List


def counting_sort(numbers: List[int], num_place: int) -> List[int]:
    len_numbers = len(numbers)
    counts = [0] * 10  # decimal
    result = [0] * len_numbers

    for num in numbers:
        counts_idx = int(num / num_place) % 10
        counts[counts_idx] += 1

    for counts_idx in range(1, 10):
        counts[counts_idx] += counts[counts_idx - 1]

    number_idx = len_numbers - 1
    while number_idx >= 0:
        counts_idx = int(numbers[number_idx] / num_place) % 10  # 0 % 10 = 0
        result[counts[counts_idx] - 1] = numbers[number_idx]
        counts[counts_idx] -= 1
        number_idx -= 1

    return result


def radix_sort(numbers: List[int]) -> List[int]:
    max_num = max(numbers)
    num_place = 1
    while max_num > num_place:
        numbers = counting_sort(numbers, num_place)
        num_place *= 10

    return numbers


if __name__ == "__main__":
    import random

    nums = [random.randint(0, 1000) for _ in range(10)]
    # nums = [24, 10, 11, 324, 201, 101, 55]
    print(radix_sort(nums))
