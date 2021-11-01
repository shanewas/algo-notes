def bubbleSort(arr):
    """ 
        this is an implementation of bubble sort

        Args:
            params1: provided array by user

        Returns:
            None

        Raises:
            KeyError: Raises an exception.
    """

    length = len(arr)

    # Traverse through all array elements
    for i in range(length):
        swapped = False

        # Last i elements are already
        #  in place
        for j in range(length-i-1):

            # traverse the array from 0 to
            # length-i-1. Swap if the element
            # found is greater than the
            # next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        # IF no two elements were swapped
        # by inner loop, then break
        if not swapped:
            break


# # Driver code to test above
# arr = [64, 34, 25, 12, 22, 11, 90]

# bubbleSort(arr)

# print("Sorted array :")
# for item in arr:
#     print("%d" % item, end=" ")
