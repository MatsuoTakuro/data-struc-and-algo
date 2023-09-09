"""
[1] => [2] => 2
[2, 3] => [2, 4] => 24
[8, 9] => [9, 0] => 90
[9, 9] => [1, 0, 0] => 100
[1, 2, 3] => [1, 2, 4] => 124
[7, 8, 9] => [7, 9, 0] => 790
[9, 9, 9] => [1, 0, 0, 0] => 1000
[9, 9, 9, 9] => [1, 0, 0, 0, 0] => 10000
[0, 0, 0, 9, 9, 9, 9] => [1, 0, 0, 0, 0] => 10000

Can not convert to string such as
l = [1, 2, 3]
print(int(''.join([str(i) for i in l])) + 1)

The number value contained in all elements is always less than 10.
The value is for the first place only.
"""
from typing import List


def remove_zero(numbers: List[int]) -> None:
    if numbers and numbers[0] == 0:  # numbers[0] (the most significant digit) is 0
        numbers.pop(0)
        # call it recursively
        remove_zero(numbers)


def list_to_int(numbers: List[int]) -> int:
    sum_numbers = 0
    for i, num in enumerate(reversed(numbers)):
        sum_numbers += num * (10**i)  # (10 to the power of i)

    return sum_numbers


def list_to_int_plus_one(numbers: List[int]) -> int:
    print(numbers)
    i = len(numbers) - 1
    numbers[i] += 1
    while 0 < i:
        if numbers[i] != 10:
            remove_zero(numbers)
            break
        # if numbers[i] == 10
        numbers[i] = 0
        numbers[i - 1] += 1
        # go to the next higher digit
        i -= 1
    else:  # numbers[0] (the highest digit) can be 10
        if numbers[0] == 10:
            numbers[0] = 1
            numbers.append(0)

    print(numbers)
    return list_to_int(numbers)


if __name__ == "__main__":
    print(list_to_int_plus_one([1]))
    print(list_to_int_plus_one([2, 3]))
    print(list_to_int_plus_one([8, 9]))
    print(list_to_int_plus_one([9, 9]))
    print(list_to_int_plus_one([7, 8, 9]))
    print(list_to_int_plus_one([9, 9, 9]))
    print(list_to_int_plus_one([0, 0, 0, 9, 9, 9, 9, 9, 9]))
