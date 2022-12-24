from typing import List


def shell_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    gap = len(numbers) // 2
    while gap > 0:
        for i in range(gap, len_numbers):
            temp_right = numbers[i]
            right_idx = i
            while right_idx >= gap and numbers[right_idx - gap] > temp_right:
                numbers[right_idx] = numbers[right_idx - gap]
                right_idx -= gap
            numbers[right_idx] = temp_right
        gap //= 2
    return numbers


if __name__ == "__main__":
    # import random
    # nums = [random.randint(0, 1000) for _ in range(10)]
    nums = [5, 6, 9, 2, 3]
    print(shell_sort(nums))
