import random
import time

def partition(arr: list, low_index: int, high_index:int) -> int:
    # O pivot é o ultimo elemento do array ou 
    pivot = arr[high_index]

    index = low_index - 1 # Index referece as posições dos valores menores

    for j in range(low_index,high_index):
        if arr[j] < pivot:
            index += 1 # Faz o swap dos elementos, trocando o maior com o menor
            arr[index],arr[j] = arr[j],arr[index]
    
    # Troca o pivot com o valor sucessor do ultimo menor
    arr[index + 1], arr[high_index] = arr[high_index],arr[index + 1] 
    return index + 1 # Retorna o pivot

def quicksort(arr, low_index, high_index):
    #Check para quando o tiver só um elemento(ou nenhum)
    if low_index < high_index:
        pivot = partition(arr,low_index,high_index) #Pega o pivot 
        quicksort(arr,low_index,pivot - 1) # Faz o sort dos menores
        quicksort(arr,pivot + 1, high_index) # Faz o sort dos maiores

start_time = time.time()

x = [random.randint(1,10000000) for x in range(5000000)]

print("--- %s seconds ---" % (time.time() - start_time))

quicksort(x,0,len(x) - 1)

print(x[:100])

print("--- %s seconds ---" % (time.time() - start_time))
