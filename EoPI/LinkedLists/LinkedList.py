# Uses Python 3
class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail




class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_next(self, node):
        if node.next_node:
            return node.next_node
        else:
            return None



def list_to_linkedlist(arr):
    head = ListNode(arr[0])
    working_node = head
    for i in range(1, len(arr)):
        new_node = ListNode(arr[i])
        working_node.next_node = new_node
        working_node = new_node
    return head




def print_linked_list(l):
    while l:
        print(l.data, end=' ')
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

if __name__ == '__main__':
    pass