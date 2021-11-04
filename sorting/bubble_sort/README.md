# Introduction

A sorting algorithm where the largest values bubble up to the top!

## Alogrithm
Bubble sort is a simple sorting algorithm. This sorting algorithm is comparison-based algorithm in which each pair of adjacent elements is compared and the elements are swapped if they are not in order. This algorithm is not suitable for large data sets as its average and worst case complexity are of Ο(n2) where n is the number of items.

<img src="https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />
     
<img src="https://www.w3resource.com/w3r_images/bubble-short.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />

```python
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

## Time Complexity
- Worst Case: O(n^2), where the array is not sorted at all
- Best Case: O(n), where the array is partiall/completely sorted. 

## Space Complexity
- Constant for both cases, as only two additional variable needs to be stored in memory, temp and swapped
