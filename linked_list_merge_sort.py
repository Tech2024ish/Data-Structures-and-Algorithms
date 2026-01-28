from linked_list import LinkedList


def merge_sort(linked_list):
    # Base case
    if linked_list is None or linked_list.head is None or linked_list.size() == 1:
        return linked_list

    left_half, right_half = split(linked_list)

    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(linked_list):
    if linked_list is None or linked_list.head is None:
        left_half = linked_list
        right_half = None
        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size//2
        mid_node = linked_list.node_at_index(mid-1)
        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half


def merge(left, right):
    merged = LinkedList()
    merged.add(0)  # fake head
    current = merged.head

    left_head = left.head
    right_head = right.head

    while left_head and right_head:
        if left_head.data < right_head.data:
            current.next_node = left_head
            left_head = left_head.next_node
        else:
            current.next_node = right_head
            right_head = right_head.next_node

        current = current.next_node

    # Attach remaining nodes
    if left_head:
        current.next_node = left_head
    else:
        current.next_node = right_head

    merged.head = merged.head.next_node  # discard fake head
    return merged


# Test example
list = LinkedList()
list.add(10)
list.add(2)
list.add(25)
list.add(100)
list.add(5)
list.add(20)

print(list)

sorted_linked_list = merge_sort(list)
print(sorted_linked_list)
