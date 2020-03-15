"""

This python code is to print the last occurance of a
particular data value(taking input from the user)
and then delete it, (bonus:- let the user give inputs and create a linked list) or
just use this sample input and check out the code

Sample input:-
LL = 1->2->3->2->4, n = 2
LL = 1->2->3->4, deleted the last occuring 2;

"""
# Import the module of linedlst where we implemented the creation of ll
import linkedlst

# Creating the linked list

data_list = []
num_of_nodes = int(input("Enter the number of nodes "))
print("Enter the data as per the number of nodes you need ")

for i in range(num_of_nodes):

    data_list.append(int(input("Enter the data value ")))

first_node = linkedlst.Node(data_list[0], ("node " + str(0 + 1)))

linkedlst.make_list(data_list, 1, num_of_nodes, first_node)

linkedlst.display(first_node, num_of_nodes)

# Where the actual code for the given problem begins.


def find_last_occurance(first_node, key):

    while first_node.next is not None:

        if first_node.next.data == key:

            key_node = first_node.next
            current_node = first_node
            alternate_node = key_node.next
        first_node = first_node.next

    delete_last_occurance(current_node, alternate_node)


def delete_last_occurance(current_node, alternate_node):

    current_node.next = alternate_node


key = int(input("Enter the data you want to delete "))
find_last_occurance(first_node, key)
linkedlst.display(first_node, num_of_nodes - 1)
