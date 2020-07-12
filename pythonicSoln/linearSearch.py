arr = [-2, -8, 6, 5, 4, 2, 3, 7, 9] 
x = int(input('enter the element you want to search:  '))


def linear_search(arr, x): 
  
    for i in range(len(arr)): 
        if arr[i] == x: 
            return i 
    return -1

output = linear_search(arr,x)

if output != -1: 
    print("Element is present at index", str(output)) 
else: 
    print("Element is not present in array") 
