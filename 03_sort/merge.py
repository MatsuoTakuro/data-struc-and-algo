from typing import List


def merge_sort(numbers: List[int]) -> List[int]:
    if len(numbers) <= 1:
        return numbers

    center = len(numbers) // 2
    left = numbers[:center]
    right = numbers[center:]

    merge_sort(left)
    merge_sort(right)

    left_idx = right_idx = nums_idx = 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            numbers[nums_idx] = left[left_idx]
            left_idx += 1
        else:
            numbers[nums_idx] = right[right_idx]
            right_idx += 1
        nums_idx += 1

    while left_idx < len(left):
        numbers[nums_idx] = left[left_idx]
        left_idx += 1
        nums_idx += 1

    while right_idx < len(right):
        numbers[nums_idx] = right[right_idx]
        right_idx += 1
        nums_idx += 1

    return numbers


if __name__ == "__main__":
    import random

    nums = [random.randint(0, 1000) for _ in range(10)]
    # nums = [5, 4, 1, 8, 7, 3, 2, 9]
    print(merge_sort(nums))
