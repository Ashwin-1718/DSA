# Bubble sort in Python

def bubbleSort(array):
    
  # loop to access each array element
  for i in range(len(array)):

    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp
  return array

data = []
max_elements=int(input("Enter no. of elements: "))
for i in range(max_elements):
  data.append(int(input(f"Enter element {i + 1}: ")))

print("Original array:", data)
sorted_arr = bubbleSort(data)
print("Sorted array:", sorted_arr)