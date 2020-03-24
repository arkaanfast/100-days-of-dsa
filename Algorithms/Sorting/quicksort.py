# A quick sort algorithm:

print("Quick sort making the last element as the pivot")


def partition(arr, low, high):

    # This function works on each partition and sorts the array

    i = low - 1
    pivot = arr[high]
    for j in range(low, high):

        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def quicksort(arr, low, high):

    if low < high:

        pivot_postition = partition(arr, low, high)

        quicksort(arr, low, pivot_postition - 1)
        quicksort(arr, pivot_postition + 1, high)


arr = [1, 45, 98, 23, 45]
print("Unsorted array => ", arr)
quicksort(arr, 0, len(arr) - 1)
print("Sorted array => ", arr)
