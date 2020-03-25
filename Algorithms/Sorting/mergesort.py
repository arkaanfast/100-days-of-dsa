print("Merge Sort ")


def mergesort(arr, low, high):

    if low < high:

        mid = (low + high) // 2
        mergesort(arr, low, mid)
        mergesort(arr, mid + 1, high)
        merge(arr, low, mid, high)


def merge(arr, low, mid, high):

    left_array = arr[low:mid + 1]
    right_array = arr[mid + 1:high + 1]

    i = j = 0
    k = low
    while i < len(left_array) and j < len(right_array):

        if left_array[i] < right_array[j]:
            arr[k] = left_array[i]
            i += 1
        else:
            arr[k] = right_array[j]
            j += 1
        k += 1

    while i < len(left_array):
        arr[k] = left_array[i]
        i += 1
        k += 1
    while j < len(right_array):
        arr[k] = right_array[j]
        j += 1
        k += 1


arr = [1, 45, 98, 23, 45]
print("Before sorting ", arr)
mergesort(arr, 0, len(arr) - 1)
print("After sorting ", arr)
