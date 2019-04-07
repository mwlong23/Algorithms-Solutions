import LinkedList as ll
import inspect

my_list = ll.ListNode()

my_list = [12,2,33,44,3]

my_linked_list = ll.list_to_linkedList(my_list)

ll.print_linked_list(my_linked_list)

print(ll.search(my_linked_list, 11))