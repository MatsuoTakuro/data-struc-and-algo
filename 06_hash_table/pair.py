from typing import List, Tuple, Optional


def get_pair(numbers: List[int], target: int) -> Optional[Tuple[int, int]]:
    # Python Set is an unordered collection of unique elements.
    # Suppose you have a list and you need only the unique items of the list you can use Python Set.
    cache = set()
    for num in numbers:
        val = target - num
        if val in cache:
            return val, num
        cache.add(num)


def get_pair_half_sum(numbers: List[int]) -> Optional[Tuple[int, int]]:
    sum_numbers = sum(numbers)
    half_sum, remainder = divmod(sum_numbers, 2)
    if remainder != 0:
        return

    cache = set()
    for num in numbers:
        val = half_sum - num
        if val in cache:
            return val, num
        cache.add(num)


if __name__ == "__main__":
    l = [11, 2, 5, 9, 10, 3]
    t = 12
    print(get_pair(l, t))
    print(get_pair_half_sum(l))
