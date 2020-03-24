# Here we will quick sort but we will keep pivot as the first element

print("Quick sort making first element as pivot")


def partition(arr, low, high):

    pivot = arr[low]
    i = low + 1
    for j in range(low + 1, high + 1):

        if arr[j] < pivot:

            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i - 1], arr[low] = arr[low], arr[i - 1]
    return (i - 1)


def quicksort2(arr, low, high):

    if low < high:

        pivot_position = partition(arr, low, high)

        quicksort2(arr, low, pivot_position - 1)
        quicksort2(arr, pivot_position + 1, high)


arr = [1, 45, 98, 23, 45]
print("Unsorted array => ", arr)
quicksort2(arr, 0, len(arr) - 1)
print("Sorted array => ", arr)
