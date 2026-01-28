def binary_search(nums, target):
    """
    Note: Binary search works only on sorted list
    """
    left, right = 0, len(nums)-1

    while left <= right:
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid-1
    return None


def verify(index):
    if index:
        print(f"\nTarget found at index: {index}")
    else:
        print("Target not found\n")


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = binary_search(nums, 6)
verify(result)

result = binary_search(nums, 12)
verify(result)
