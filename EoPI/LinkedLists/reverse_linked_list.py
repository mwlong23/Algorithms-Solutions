import LinkedList as ll

fibbonacci = [1,1,2,3,5,8]

new_linked_list = ll.list_to_linkedlist(fibbonacci)

# ll.print_linked_list(new_linked_list)

def print_reversed_linked_list(head):
    nodes = []

    while head:
        nodes.append(head)
        head = head.next_node
    print()
    while nodes:
        print(nodes.pop().data, end=' ')

# print_reversed_linked_list(new_linked_list)


# TODO:bug - existst, last element of queue added endlessly
def revrese_linked_list(head):
    nodes = []

    while head:
        nodes.append(head)
        head = head.next_node
    # Reset next_node to None to prevent last item looping on itself
    for node in nodes:
        node.next_node = None

    new_head = dummy_head = ll.ListNode(0)
    nodes = nodes[::-1]

    new_head.next_node = nodes[0]
    for i in range(len(nodes)-1):
        nodes[i].next_node = nodes[i+1]



    return dummy_head.next_node

rev = revrese_linked_list(new_linked_list)
ll.print_linked_list(rev)

