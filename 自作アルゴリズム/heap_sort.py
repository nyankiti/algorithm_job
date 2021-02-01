def left(i):
    return i*2+1
 
def right(i):
    return i*2+2
 
def parent(i):
    return (i-1)/2
 
def heapify(data):
    last = (len(data)-1)/2
    for i in range(last,0,-1):
        while True:
            if left(i) < len(data) and data[i] > data[left(i)]:
                data[i], data[left(i)] = data[left(i)], data[i]
            if right(i) < len(data) and data[i] > data[right(i)]:
                data[i], data[right(i)] = data[right(i)], data[i]
            if i == 0:
                break
            i = parent(i)
    return data
 
def heap_sort(data):
    result = []
    data = heapify(data)
    for i in range(len(data)):
        result.append(data.pop(0))
        data = heapify(data)
    return result
 
data = [42, 21, 10, 2, 30, 51, 80, 90, 18, 56, 50, 25, 15, 95, 44, 69]
 
data = heap_sort(data)
 
print(data)
