arr = [-2, -8, 6, 5, 4, 2, 3, 7, 9]  
x = int(input('enter the element you want to search:  '))
n = len(arr)

def interpolationSearch(arr, n, x): 
    low = 0
    high = (n - 1) 
   
    while low <= high and x >= arr[low] and x <= arr[high]: 
        if low == high: 
            if arr[low] == x:  
                return low; 
            return -1; 
          
        pos  = low + int(((float(high - low) / 
            ( arr[high] - arr[low])) * ( x - arr[low]))) 
  
        if arr[pos] == x: 
            return pos 

        if arr[pos] < x: 
            low = pos + 1; 

        else: 
            high = pos - 1; 
      
    return -1

output = interpolationSearch(arr, n, x) 
  
if output != -1: 
    print("Element found at index",output)
else: 
    print("Element not found")