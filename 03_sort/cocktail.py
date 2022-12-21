from typing import List

def cocktail_sort(numbers: List[int]) -> List[int]:
  len_numbers = len(numbers)
  swapped = True
  start_index = 0
  end_index = len_numbers - 1
  while swapped:
      swapped = False
      for i in range(start_index, end_index):
        if numbers[i] > numbers[i+1]:
          numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
          swapped = True

      if not swapped:
          break

      swapped = False
      end_index = end_index - 1

      for i in range(end_index-1, start_index-1, -1): # for example, loop 4 times, decreasing by -1 from 3 until it reaches -1.
        if numbers[i] > numbers[i+1]:
          numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
          swapped = True

      start_index = start_index + 1
  return numbers


if __name__ == '__main__':
  import random
  nums = [random.randint(0, 1000) for i in range(10)]
  print(cocktail_sort(nums))
