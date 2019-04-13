import LinkedList as ll


l1 = ll.list_to_linkedlist([2,5,7])
l2 = ll.list_to_linkedlist([3,11,15])

def merge_two_sorted_list(list1,list2):
    # Create placeholder for result
    dummy_head = tail = ll.ListNode()

    while list1 and list2:
        if list1.data < list2.data:
            tail.next_node, list1 = list1,list1.next_node

        else:
            tail.next_node, list2 = list2, list2.next_node

        tail = tail.next_node

    tail.next_node = list1 or list2
    return dummy_head.next_node

ll.print_linked_list(merge_two_sorted_list(l1,l2))