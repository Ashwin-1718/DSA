def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1


# -------- Main Program --------

n = int(input("How many values you want to insert? "))

arr = []
for i in range(n):
    val = int(input(f"Enter value {i+1}: "))
    arr.append(val)

# Sort the list
arr.sort()
print("Sorted list:", arr)

key = int(input("Enter value to search: "))

result = binary_search(arr, key)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")