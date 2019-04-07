# Uses Python 3

class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next_node = next_node



def list_to_linkedList(arr):
    ll = ListNode()
    print(ll)
    working_node = ll
    for el in arr:
        working_node.next_node = ListNode(el)
        working_node = working_node.next_node
    return ll

def print_linked_list(l):
    while l:
        print(l.data)
        l = l.next_node


def search(linked_list, key):

    while linked_list and linked_list.data != key:
        linked_list = linked_list.next_node
    return linked_list


def insert_after(node, new_node):
    new_node.next_node = node.next_node
    node.next_node = new_node


def delete_after(node):
    node.next_node = node.next_node.next_node

