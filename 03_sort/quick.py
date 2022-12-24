from typing import List


def partition(numbers: List[int], low_idx: int, high_idx: int) -> int:
    swapped_idx = low_idx - 1
    pivot = numbers[high_idx]
    for left_idx in range(low_idx, high_idx):
        if numbers[left_idx] <= pivot:
            swapped_idx += 1
            numbers[swapped_idx], numbers[left_idx] = (
                numbers[left_idx],
                numbers[swapped_idx],
            )
    numbers[swapped_idx + 1], numbers[high_idx] = pivot, numbers[swapped_idx + 1]
    return swapped_idx + 1


def quick_sort(numbers: List[int]) -> List[int]:
    def _quick_sort(numbers: List[int], low_idx: int, high_idx: int) -> None:
        if low_idx < high_idx:
            partition_idx = partition(numbers, low_idx, high_idx)
            _quick_sort(numbers, low_idx, partition_idx - 1)
            _quick_sort(numbers, partition_idx + 1, high_idx)

    _quick_sort(numbers, 0, len(numbers) - 1)
    return numbers


if __name__ == "__main__":
    import random

    nums = [random.randint(0, 1000) for _ in range(10)]
    # nums = [1, 8, 3, 9, 4, 5, 7]
    print(quick_sort(nums))
