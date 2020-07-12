arr = [-2, -8, 6, 5, 4, 2, 3, 7, 9]   


def merge_Sort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 
        L = arr[:mid]  
        R = arr[mid:]
  
        merge_Sort(L) 
        merge_Sort(R) 
  
        i = j = k = 0
          
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+= 1
            else: 
                arr[k] = R[j] 
                j+= 1
            k+= 1
          
        while i < len(L): 
            arr[k] = L[i] 
            i+= 1
            k+= 1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+= 1
            k+= 1
  

merge_Sort(arr) 
print("Sorted array is: ", ) 
for i in range(len(arr)):         
    print(arr[i]) 
    