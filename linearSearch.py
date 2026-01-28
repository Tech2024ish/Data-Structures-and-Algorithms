def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i

    return -1


def verify(index):
    if not index:
        print("\nTarget not found\n")
    else:
        print(f"\nTarget found at index: {index}\n")


# Test example
nums = [2, 1, 4, 6, 30, 20, 21, 12]
target = 4
result = linear_search(nums, target)
verify(result)
