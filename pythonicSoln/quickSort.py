arr = [-2, -8, 6, 5, 4, 2, 3, 7, 9]
n = len(arr) 

def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     
  
    for j in range(low , high): 
        if   arr[j] <= pivot:  
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
   
def quick_Sort(arr,low,high): 
    if low < high: 
        pi = partition(arr,low,high) 
        quick_Sort(arr, low, pi-1) 
        quick_Sort(arr, pi+1, high) 

quick_Sort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print (arr[i]), 