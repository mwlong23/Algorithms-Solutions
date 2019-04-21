# Use Python 3
# By Mitch Long - 2019

# Implements an algorithm that checks for cycles in a Linked List

import LinkedLists.LinkedList as ll

def is_cyclic(head):
    if head.next_node == None:
        return False

    visited = {}
    visiting = head

    while visiting:
        if visiting.data not in visited:
            visited[visiting.data] = 1
            visiting = visiting.next_node
        else:
            return True
    return False


if __name__ == '__main__':
    ascending_list = [1,2,3,4,5,6,7,8]
    ll_head = ll.list_to_linkedlist(ascending_list)

    # prev_node = current_node

