def recursive_bubble_sort(arr):
    if len(arr) <= 1:
        return arr
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return recursive_bubble_sort(arr[:-1]) + [arr[-1]]
