import random
import time

def partition(arr, low_index, high_index):
    pivot = arr[high_index]

    index = low_index - 1

    for j in range(low_index,high_index):
        if arr[j] < pivot:
            index += 1
            arr[index],arr[j] = arr[j],arr[index]
    
    arr[index + 1], arr[high_index] = arr[high_index],arr[index + 1]
    return index + 1

def quicksort(arr, low_index, high_index):
    if low_index < high_index:
        pivot = partition(arr,low_index,high_index)
        quicksort(arr,low_index,pivot - 1)
        quicksort(arr,pivot + 1, high_index)


start_time = time.time()

x = [random.randint(1,10000000) for x in range(1000000)]

print("--- %s seconds ---" % (time.time() - start_time))

quicksort(x,0,len(x) - 1)

print(x[:100])

print("--- %s seconds ---" % (time.time() - start_time))
