def buuble_sort(arr):
    n = len(arr)
    for i in range(n - 1):           
        swapped = False
        for j in range(n - 1 - i):   
            if arr[j] < arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:   
            break
    return arr


size = int(input("Enter the number of elements: "))
numbers = []

for i in range(size):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)

print("\nOriginal list:", numbers)

sorted_list = buuble_sort(numbers)

print("Sorted list in Descending order:", sorted_list)