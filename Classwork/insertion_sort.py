def insertion_sort(arr):
  for i in range(1,len(arr)):
    key=arr[i]
    j=i-1

    while j>=0 and arr[j]>key:
      arr[j+1]=arr[j]
      j=j-1
    
    arr[j+1]=key

data = []
max_elements=int(input("Enter no. of elements: "))
for i in range(max_elements):
  data.append(int(input(f"Enter element {i + 1}: ")))

print("Original array:", data)
insertion_sort(data)
print("Sorted array:", data)
