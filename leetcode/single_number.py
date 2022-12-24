from typing import List

# https://leetcode.com/problems/single-number/submissions/
def singleNumber(nums: List[int]) -> int:
    uniq_num = 0
    for i in nums:
        uniq_num ^= i
    # for example, nums is assumed as [1, 2, 4, 2, 1]
    # uniq_num xor i will be expressed bitwise below
    # i = 1
    #   (000)2 xor (001)2 = (001)2 = (1)10
    # i = 2
    #   (001)2 xor (010)2 = (011)2 = (3)10
    # i = 4
    #   (011)2 xor (100)2 = (111)2 = (7)10
    # i = 2
    #   (111)2 xor (010)2 = (101)2 = (5)10
    # i = 1
    #   (101)2 xor (001)2 = (100)2 = (4)10

    # can xor nums at all
    #     (001)2
    #     (010)2
    #     (100)2
    #     (010)2
    #     (001)2
    # xor)------
    #     (100)2

    return uniq_num


if __name__ == "__main__":

    numbers = [1, 2, 4, 2, 1]
    print(numbers)
    print(singleNumber(numbers))
