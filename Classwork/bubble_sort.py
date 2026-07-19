def bubble_sort(data):
    for i in range(no_elements):
        print(f"----Pass {i + 1}----")
        for j in range(0,len(data)-i-1):
            if data[j]>data[j+1]:
                temp=data[j]
                data[j]=data[j+1]
                data[j+1]=temp
        print(data)
    return data


unsorted_data=[]
no_elements=int(input("Enter no. of elements: "))
for i in range(no_elements):
    item=int(input(f"Enter item {i+1}: "))
    unsorted_data.append(item)

print("----Data before sorting-----")
for i in unsorted_data:
    print(i)

sorted_data=bubble_sort(unsorted_data)

print("----Data after sorting-----")
for i in sorted_data:
    print(i)
