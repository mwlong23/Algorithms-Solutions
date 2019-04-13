# Reverses a sublist of a linked List

import LinkedList as ll

list_m = ll.list_to_linkedlist([11,3,5,2,6,7,8,9,10])

def reverse_sublist(linked_list,s,f):
    dummy_head = sublist_head = ll.ListNode(0,linked_list)

    # Sets sublist_head to node before s
    for _ in range(1,s):
        sublist_head = sublist_head.next_node

    # Sets sublist_itter to Node at s
    sublist_itter = sublist_head.next_node
    for _ in range(f-s):
        temp = sublist_itter.next_node
        sublist_itter.next_node = temp.next_node
        temp.next_node = sublist_head.next_node
        sublist_head.next_node = temp
    return dummy_head.next_node


ll.print_linked_list(reverse_sublist(list_m,3,5))