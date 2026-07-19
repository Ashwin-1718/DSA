def quick_sort(arr):
  if len(arr)<=1:
    return arr
  pivot=arr[len(arr)//2]
  left=[x for x in arr if x < pivot]  
  middle=[x for x in arr if x == pivot]
  right=[x for x in arr if x > pivot]
  return quick_sort(left)+middle+quick_sort(right)

arr = []
max_elements=int(input("Enter no. of elements: "))
for i in range(max_elements):
  arr.append(int(input(f"Enter element {i + 1}: ")))

print("Original array:", arr)
arr=quick_sort(arr)
print("Sorted array:", arr)