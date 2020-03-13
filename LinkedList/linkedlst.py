class Node:

    def __init__(self, data, name):

        self.name = name
        self.data = data
        self.next = None

    def __str__(self):

        return self.name


def make_list(data, num, total_nodes, first_node):

    if num == total_nodes:
        print("Done converting the array to linked List")
    else:
        new_node = Node(data[num], "node " + str(num + 1))
        first_node.next = new_node
        make_list(data, (num + 1), total_nodes, new_node)


def display_node(first_node):
    for row in range(1, 5):
        if row == 1 or row == 3:
            print("=" * 25)

        elif row == 2:
            print(first_node.data, end=" ")
            print("|", end="  ")
            print("Pointing to " + str(first_node.next))

        elif row == 4:
            print(" ", end="")
            print(first_node)

        else:
            print(" " * 3, end="")
            print("|")


def display(first_node, num_of_nodes):

    for nodes in range(1, num_of_nodes + 1):
        display_node(first_node)
        first_node = first_node.next


data_list = []
num_of_nodes = int(input("Enter the number of nodes "))
print("Enter the data as per the number of nodes you need ")

for i in range(num_of_nodes):

    data_list.append(int(input("Enter the data value ")))

first_node = Node(data_list[0], ("node " + str(0 + 1)))

make_list(data_list, 1, num_of_nodes, first_node)

display(first_node, num_of_nodes)
