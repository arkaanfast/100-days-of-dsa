class Fenwick:

    def __init__(self, size):

        self.BIT = [0] * (size + 1)
        self.size = size
    
    def updateBIT(self, index, val):

        index += 1

        while index <= self.size:

            self.BIT[index] += val

            index += (index & -index)
        
        

    def get_sum(self, end):

        end += 1
        s = 0
        while end > 0:

            s += self.BIT[end]
            end -= (end & -end)
    
        return s
    

    def construct_BIT(self, arr):

        for i in range(self.size):

            self.updateBIT(i, arr[i])

        print("The fenwick tree is :-", self.BIT)


bit = Fenwick(12)

arr = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]

bit.construct_BIT(arr)

print(bit.get_sum(5))

