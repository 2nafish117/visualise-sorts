from Settings import basicStep

def quickSort(array, low, high):
    if low < high:
        p = partition(array, low, high)
        quickSort(array, low, p)
        quickSort(array, p + 1, high)

def partition(array, low, high):
    pivot = array[low]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while i <= high and array[i] < pivot:
            i += 1
        j -= 1
        while j >= low and array[j] > pivot:
            j -= 1
        
        if i >= j:
            return j
        array[i], array[j] = array[j], array[i]
        basicStep()
