class MaxHeap:


    def __init__(self, capacity):

        self.capacity = capacity
        self.heap = [0] * self.capacity
        self.size = 0

    
    def get_left_child_index(self, index):

        return (2 * index) + 1

    def get_right_child_index(self, index):

        return (2 * index) + 2

    def get_parent_index(self, index):

        return (index - 1) // 2

    def has_left_child(self, index):

        return True if self.get_left_child_index(index) < self.size else False

    def has_right_child(self, index):

        return True if self.get_right_child_index(index) < self.size else False

    def has_parent(self, index):

        return True if self.get_parent_index(index) >= 0 else False

    def get_left_child(self, index):

        return self.heap[self.get_left_child_index(index)]

    def get_right_child(self, index):

        return self.heap[self.get_right_child_index(index)]

    def get_parent(self, index):

        return self.heap[self.get_parent_index(index)]

    def swap(self, index_1, index_2):

        self.heap[index_1], self.heap[index_2] = self.heap[index_2], self.heap[index_1]

    
    def if_full(self):

        if self.size == self.capacity:
            return False
        else:
            return True

    def peek(self):

        return self.heap[0]

    def insert(self, element):

        if self.if_full():
            self.heap[self.size] = element
            self.size += 1
            self.heapify_up()
        else:
            print("Capacity is full")

    def delete(self):

        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heapify_down()

    def heapify_up(self):

        index = self.size - 1
        while self.has_parent(index) and self.get_parent(index) < self.heap[index] :
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)

        

    def heapify_down(self):

        index = 0
        while self.has_left_child(index):
            greater_child_index = self.get_left_child_index(index)
            if self.get_right_child_index(index) > self.get_left_child_index(index):
                greater_child_index = self.get_right_child_index(index)

            if self.heap[index] > self.heap[greater_child_index]:

                break
            
            if self.heap[index] < self.heap[greater_child_index]:

                self.swap(index, greater_child_index)

            index = greater_child_index


max_heap = MaxHeap(5)

max_heap.insert(10)
max_heap.insert(20)
max_heap.insert(25)
max_heap.insert(11)
max_heap.insert(9)

print("MAX HEAP IS ")

for element in max_heap.heap:

    if element != 0:
        print(element, end=" ")
