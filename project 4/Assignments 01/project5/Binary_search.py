def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        guess = arr[mid]

        if guess == target:
            return mid
        elif guess < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # target not found


# Example usage:
numbers = [1, 3, 5, 7, 9, 11, 15, 18, 21]
target = 7

result = binary_search(numbers, target)

if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print(f"Target {target} not found in the list")
