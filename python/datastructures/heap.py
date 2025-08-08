def heapify(arr : list, size: int, i : int):
    largest = i
    left_child = i * 2 + 1
    right_child = i * 2 + 2

    if size > left_child and arr[left_child] > arr[largest]:
        largest = left_child
    if size > right_child and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr,size,largest)

def max_heap(arr):
    size = len(arr)
    for i in range(size // 2 - 1 ,-1,-1):
        heapify(arr,size,i)

def insert(arr,value):
    arr.append(value)
    current_index = len(arr) - 1
    while current_index > 0:
        parent = (current_index - 1) // 2
        if arr[parent] < arr[current_index]:
            arr[parent], arr[current_index] = arr[current_index], arr[parent]
            current_index = parent
        else:
            break

def delete(arr,value):
    for current_value in arr:
        if current_value == value:
            i = arr.index(current_value)
            break
    if i == None:
        return None
    
    arr[i], arr[-1] = arr[-1], arr[i]
    arr.pop()
    if i < len(arr):
        heapify(arr,len(arr),i)


arr = [0,6,32,2,1,65,7]
max_heap(arr)
print(arr)
insert(arr,53)
print(arr)
delete(arr,65)
insert(arr,64)
insert(arr,23)
print(arr)
