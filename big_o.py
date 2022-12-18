# O(log(n))
def func2(n):
  if n <= 1:
    return
  else:
    print(n)
    func2(n/2)
# func2(10)

# O(n)
def func3(numbers):
  for num in numbers:
    print(num)
# func3([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# O(n * log(n))
def func4(n):
  # n
  for i in range(int(n)):
    print(i, end= ' ')
  print()
  # *
  # log(n)
  if n <= 1:
    return
  func4(n/2)
func4(10)

# O(n**2)
def func5(numbers):
  # n
  for i in range(len(numbers)):
    # *
    # n
    for j in range(len(numbers)):
      print(numbers[i], numbers[j])
    print()
# func5([1, 2, 3, 4, 5])
