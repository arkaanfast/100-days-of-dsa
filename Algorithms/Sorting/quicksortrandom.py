# This qucik sort is considered to me the more efficient quick sort algo
# Compare to the other two
# I will implement this using Lomuto's swapping technique

from random import randint

print("Quick sort with some random pivot :) ")


def partition(arr, low, high):

    i = low - 1
    pivot = arr[high]
    for j in range(low, high):

        if arr[j] < pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def random_partition(arr, low, high):

    random_position = randint(low, high)
    arr[random_position], arr[high] = arr[high], arr[random_position]
    return partition(arr, low, high)


def quick_sort_random(arr, low, high):

    if low < high:

        pivot_position = random_partition(arr, low, high)
        quick_sort_random(arr, low, pivot_position - 1)
        quick_sort_random(arr, pivot_position + 1, high)


arr = [1, 45, 98, 23, 45]
print("Unsorted array => ", arr)
quick_sort_random(arr, 0, len(arr) - 1)
print("Sorted array => ", arr)
