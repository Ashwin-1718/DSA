# Function to find the index of the minimum element in the unsorted part
def minimum(arr, start):
    min_index = start
    for i in range(start + 1, len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i
    return min_index

# Function to perform selection sort
def selection_sort(arr):
    for i in range(len(arr) - 1):
        # Find the index of the minimum element in the unsorted part
        min_index = minimum(arr, i)
        
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

data = []
max_elements=int(input("Enter no. of elements: "))
for i in range(max_elements):
  data.append(int(input(f"Enter element {i + 1}: ")))

print("Original array:", data)
sorted_arr = selection_sort(data)
print("Sorted array:", sorted_arr)