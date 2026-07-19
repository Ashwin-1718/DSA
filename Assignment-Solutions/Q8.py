def selection_sort(s):
    arr = list(s)   
    n = len(arr)

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:   
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return "".join(arr)   


user_input = input("Enter a string: ")
sorted_string = selection_sort(user_input)

print("Original string:", user_input)
print("Sorted string (Selection Sort):", sorted_string)