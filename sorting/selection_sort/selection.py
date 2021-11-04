def selection_sort(arr):
    """
    This function performs a selection sort on the given array.
    """
    # Iterate over the array
    for i in range(len(arr)):
        # Find the smallest element in the unsorted array
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the smallest element with the current element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
