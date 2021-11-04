# How to implement it recursively?

Recursive Bubble Sort has no performance/implementation advantages, but can be a good question to check one’s understanding of Bubble Sort and recursion.
If we take a closer look at Bubble Sort algorithm, we can notice that in first pass, we move largest element to end (Assuming sorting in increasing order). In second pass, we move second largest element to second last position and so on.

## Algorithm

Base Case: If array size is 1, return.
Do One Pass of normal Bubble Sort. This pass fixes last element of current subarray.
Recur for all elements except last of current subarray.

<img src="https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />

<img src="https://www.w3resource.com/w3r_images/bubble-short.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />

```python

def recursive_bubble_sort(arr):
    if len(arr) <= 1:
        return arr
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return recursive_bubble_sort(arr[:-1]) + [arr[-1]]

```

## Time Complexity

- Worst Case: O(n^2), where the array is not sorted at all
- Best Case: O(n), where the array is partiall/completely sorted.

## Space Complexity

- Constant for both cases, as only two additional variable needs to be stored in memory, temp and swapped
