def heapify(merged, current_index, length):


    if current_index >= length:
        return

    left_child_index = 2 * current_index + 1
    right_child_index = 2 * current_index + 2
    max_index = 0

    if left_child_index < length and merged[left_child_index] > merged[current_index]:

        max_index = left_child_index
    
    else:
        max_index = current_index

    if right_child_index < length and merged[right_child_index] > merged[max_index]:

        max_index = right_child_index

    if max_index != current_index:

        merged[max_index], merged[current_index] = merged[current_index], merged[max_index]
        heapify(merged, max_index, length)


def build_max_heap(merged, n):

    for i in range((n // 2) - 1, -1, -1):

        heapify(merged, i, n)

    
def merge_heaps(merged, heap_1, heap_2, length_1, lenght_2):

    for i in range(length_1):

        merged[i] = heap_1[i]

    for j in range(length_2):

        merged[length_1 + j] = heap_2[j]
        
    build_max_heap(merged, length_1 + lenght_2)

# Driver program 

heap_1 = [10, 5, 6, 2]
heap_2 = [12, 7, 9]

length_1 = len(heap_1)
length_2 = len(heap_2)

merged = [0] * (length_1 + length_2)
merge_heaps(merged, heap_1, heap_2, length_1, length_2)

for i in range(len(merged)):

    print(merged[i], end=" ")