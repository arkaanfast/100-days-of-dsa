# Given a binary tree :- Create a linked list at each depth i.e if the depth is 3 then there should be three linked lists

from tree import Tree_Node


class Node:

    def __init__(self, data):

        self.data = data
        self.next = None


def ll_at_depth(root, lists, depth):

    if root is None:
        return

    if len(lists) == depth:

        new_ll = []
        new_node = Node(root.data)
        new_ll.append(new_node)
        lists.append(new_ll)
    else:
        ll = lists[depth]
        node = ll.pop()
        if node is not None:
            node.next = Node(root.data)
            ll.append(node)
        else:
            pass

    ll_at_depth(root.left, lists, depth + 1)
    ll_at_depth(root.right, lists, depth + 1)
    return lists

# The display is only for diplaying the linked lists just for checking if its converting a bt:


def display_ll(lists):
    for ll in lists:
        for node in ll:
            while node is not None:
                print(node.data, end="=>")
                node = node.next

            print("null")


tn = Tree_Node(1)
tn.left = Tree_Node(2)
tn.right = Tree_Node(5)
tn.left.left = Tree_Node(4)
lists = []
ll_lists = ll_at_depth(tn, lists, 0)
display_ll(ll_lists)
