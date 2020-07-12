array = [-2, -6, 6, 7, 45, 2]
n = len(array)


def insertion_sort(array):
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = key


insertion_sort(array)
print('Sorted array is:')
for i in range(0, n):
    print(array[i])
