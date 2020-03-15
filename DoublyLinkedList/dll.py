class Node:

    def __init__(self, data, name):

        self.name = name
        self.prev = None
        self.data = data
        self.next = None

    def __str__(self):

        return self.name


def make_dll(data, root_node, num, total_nodes):

    if num == total_nodes:
        return "Done Converting"

    else:
        new_node = Node(data[num], "node " + str(num + 1))
        root_node.next = new_node
        new_node.prev = root_node
        make_dll(data, new_node, num + 1, total_nodes)


def display_node(root_node):
    for row in range(1, 5):
        if row == 1 or row == 3:
            print("=" * 47)

        elif row == 2:
            print("Pointing to " + str(root_node.prev), end=" ")
            print("|", end="  ")
            print(root_node.data, end=" ")
            print("|", end="  ")
            print("Pointing to " + str(root_node.next))

        elif row == 4:
            print(" ", end="")
            print(root_node)


def display(root_node, num_of_nodes):

    for nodes in range(1, num_of_nodes + 1):
        display_node(root_node)
        root_node = root_node.next


data_list = []
num_of_nodes = int(input("Enter the number of nodes "))
print("Enter the data as per the number of nodes you need ")

for i in range(num_of_nodes):

    data_list.append(int(input("Enter the data value ")))

root_node = Node(data_list[0], ("node " + str(0 + 1)))

make_dll(data_list, root_node, 1, num_of_nodes)

display(root_node, num_of_nodes)
