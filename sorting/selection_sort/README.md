## Introduction

Similar to bubble sort, but instead of first placing largest values at the end, we will place smallest values at the start.

## Algorithm

- Store the index of first element in a variable minIndex.
- Take one pointer i which will start from the beginning of the array and loop through the whole length.
- Take another pointer j which will start from the next element of the current location of the first pointer.Loop thorough the end of the array. If any element is smaller than the first element, keep replacing the value of minIndex with that index. This way, we find the index of the minimum number.
- If value of i doesn't match with minIndex, swap their elements.
- Keep on looping
- return the sorted array

<img src="https://upload.wikimedia.org/wikipedia/commons/9/94/Selection-Sort-Animation.gif"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />

<img src="https://www.w3resource.com/w3r_images/selection-short.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />

```python

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
```

## Time Complexity

- Worst Case: O(n^2)
- Best Case: O(n^2), no change. As we are traversing the whole array either way

## Space Complexity

- Constant for both cases

## Special Note

Both bubble and selection sort is bad, but in some cases, selection sort is better to use than using bubble sort. For example if you want to reduce the number of **swap** operation, selection sort is better.
