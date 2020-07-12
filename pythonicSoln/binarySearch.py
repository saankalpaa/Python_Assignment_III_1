arr = [-2, -8, 6, 5, 4, 2, 3, 7, 9]  
x = int(input('enter the element you want to search:  '))

def binary_search(arr, low, high, x): 
  
    if high >= low: 
        mid = (high + low) // 2
        if arr[mid] == x: 
            return mid 
  
        elif arr[mid] > x: 
            return binary_search(arr, low, mid - 1, x) 
   
        else: 
            return binary_search(arr, mid + 1, high, x) 
  
    else: 
        return -1
   
output = binary_search(arr, 0, len(arr)-1, x) 
  
if output != -1: 
    print("Element is present at index", str(output)) 
else: 
    print("Element is not present in array") 
