def bubble_sort(array):
    isSorted = False
    passes = 0
    length = len(array)
    while not isSorted:
        isSorted = True
        # perform a pass through the array
        # excluding already sorted positions
        for i in range(length-1-passes):
            if array[i] > array[i+1]:
                swap(i, i+1, array)
                # array is not sorted yet
                isSorted = False
        passes += 1
    return array
def swap(i, j, array):
    # Swap values at indexes i and j
    array[i], array[j] = array[j], array[i]