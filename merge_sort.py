def merge_sort(list):
    """
    Divide: Recursively split the large list into sublist based on the mitpont
    Conqer: Recursively sort each sublist separately
    Merge: Recursively combines two sublists into one large list
    Runs in O(n log n) time
    """
    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):
    """
    Recursively find the midpoint and split list into 
    two sublists left and list returns left and right 
    It runs in O(n) time 
    """
    midpoint = len(list)//2
    left = list[:midpoint]
    right = list[midpoint:]
    return left, right


def merge(left, right):
    """
    Merge: Recursively combines two sublists into 
    one large list and return merged list
    Runs in O(log n) time
    """
    merged_list = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1

    while i < len(left):
        merged_list.append(left[i])
        i += 1

    while j < len(right):
        merged_list.append(right[j])
        j += 1

    return merged_list

# This is ahelper function for verify


def verify(list):
    n = len(list)
    if n == 0 or n == 1:
        return True
    return list[0] <= list[1] and verify(list[1:])


numbers = [20, 10, 15, 23, 25, 35, 32, 19, 20, 9, 5, 31, 12]
result = merge_sort(numbers)
print(verify(numbers))
print(verify(result))
