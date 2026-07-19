global no_array, no_elements
no_array=[]

def main():
  global no_array, no_elements
  no_elements=int(input("Enter no. of Elements : "))
  for i in range(no_elements):
    item=int(input(f"Enter item {i + 1}: "))
    no_array.append(item)

  no_array.sort()

  print("_____After Sorting______")
  for i in range(len(no_array)):
    print(no_array[i])

  search_value=int(input("Enter the search value : "))

  loc=binary_search(search_value)

  if loc==-1:
    print("Element not found!")
  else:
    print("Element found in loc: ", loc)

def binary_search(search_value):
  beg=0
  end = no_elements - 1
  loc = -1
  while beg<=end:
    mid = (beg + end) // 2
    if no_array[mid] == search_value:
      loc = mid
      return loc
    elif search_value < no_array[mid]:
      end = mid - 1
    else:
      beg = mid + 1
  return loc

main()