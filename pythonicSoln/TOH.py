def toh(n , source, destination, auxilliary): 
    if n==1: 
        print("Move disk 1 from source",source,"to destination",destination) 
        return
    toh(n-1, source, auxilliary, destination) 
    print("Move disk",n,"from source",source,"to destination",destination) 
    toh(n-1, auxilliary, destination, source) 
          
n = 4
toh(n,'A','B','C')  