
import heapq

numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]

heapq.heapify(numbers)

print(numbers)


print(heapq.nlargest(3, numbers))
print(heapq.nsmallest(3, numbers))
