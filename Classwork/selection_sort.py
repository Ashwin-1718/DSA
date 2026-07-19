def selection_sort()
unsorted_data=[]
no_elements=int(input("Enter no. of elements: "))

for i in range(no_elements):
    value=int(input(f"Enter element {i + 1}: "))
    unsorted_data.append(value)

print("----Before sorting----")
for i in unsorted_data:
    print(unsorted_data[i])

sorted_data=selection_sort(unsorted_data)

print("----After sorting----")
for i in sorted_data:
    print(sorted_data[i])

