def soma(arr):
    if not arr:
        return 0
    return arr[0] + soma(arr[1:])

def count(arr):
    if not arr:
        return 0
    return 1 + count(arr[1:])

def biggest(arr,max):
    if not arr and max > 0:
        return max
    if arr[0] > max:
        max = arr[0]
    return biggest(arr[1:],max)
    
x = [2,5,3,100,6,2,20,4]

print(biggest(x,0))