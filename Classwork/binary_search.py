global no_array,no_elements
no_array=[]

def main():
    global no_array,no_elements
    no_elements=int(input("Enter no. of elements:"))

    for i in range(no_elements):
        item=int(input(f"Enter element {i+1}:"))
        no_array.append(item)

    no_array.sort()

    print("----Elements after sorting----")
    for i in range(len(no_array)):
        print(no_array[i])

    search_value=int(input("Enter search value: "))

    loc=binary_search(search_value)

    if loc==-1:
        print("Element not found")
    else:
        print("Element found at location",loc+1)


def binary_search(search_value):
    loc=-1
    beg=0
    end = no_elements - 1
    while beg<=end:
        mid = (beg + end) // 2
        if search_value == no_array[mid]:
            loc=mid
            return loc
        elif search_value > no_array[mid]:
            beg = mid + 1
        else:
            end = mid - 1
    return loc

main()