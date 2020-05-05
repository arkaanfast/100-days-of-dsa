# Implementing inversion count using BIT (Fenwick tree)
# Time complexity O(nlogn)
# Space complexity O(n)


def get_sum(bit, index):
    # This finds the number of elements greater than the element at (index + 1)
    sum = 0
    while index > 0:

        sum += bit[index]
        index -= index & (-index)

    return sum


def update_tree(bit, index, val, tree_len):

    while index <= tree_len:

        bit[index] += val
        index += index & (-index)


def inversion_count(main_arr, arr_len):

    inv_count = 0
    max_element = max(main_arr)

    bit = [0] * (max_element + 1)

    for i in range(arr_len - 1, -1, -1):
        # Here we will be counting the number of elements added before the current element if added then
        # there is inversion else its not there
        inv_count += get_sum(bit, main_arr[i] - 1)
        # Update the tree and add the current element into the tree as well as thier ancestors
        update_tree(bit, arr[i], 1, max_element)

    return inv_count


# Driver function taking a sample input
arr = [8, 4, 2, 1]
print(f"The array is {arr}")
print("The inversion count is", inversion_count(arr, len(arr)))