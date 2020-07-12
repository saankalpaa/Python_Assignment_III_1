array = [-2, -8, 6, 5, 4, 2, 3, 7, 9]
n = len(array)


def bubble_sort(array):
    for i in range(0, n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            else:
                pass


bubble_sort(array)
print('Sorted array is:')
for i in range(0, n):
    print(array[i])


