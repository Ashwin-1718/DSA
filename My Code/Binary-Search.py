def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid   # element found
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1   # not found


# Main program
size = int(input("Enter the size of the list: "))
arr = []

print(f"Enter {size} numbers (any order):")
for i in range(size):
    num = int(input(f"Enter element {i+1}: "))
    arr.append(num)

# Sort the list
arr.sort()
print("\nSorted list:", arr)

target = int(input("\nEnter the number you want to search: "))

result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")
