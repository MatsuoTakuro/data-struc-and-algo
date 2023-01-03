import heapq

words = ["python", "java", "go", "python", "c", "go", "python"]

numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
numbers2 = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heap_data = []

print(numbers)
heapq.heapify(numbers)
print(numbers)
print(heapq.nlargest(3, numbers))  # we will implement this using other methods!
print(heapq.nsmallest(3, numbers))
while numbers:
    print(heapq.heappop(numbers))

print(numbers2)
for num in numbers2:
    heapq.heappush(heap_data, num)
print(heap_data)
while heap_data:
    print(heapq.heappop(heap_data))
