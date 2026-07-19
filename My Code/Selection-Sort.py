def selection_sort(s):
    arr = list(s)   # convert string to list of characters
    n = len(arr)

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:   # compare characters
                min_index = j
        # Swap smallest character
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return "".join(arr)   # convert back to string


# ---- Main Program ----
user_input = input("Enter a string: ")
sorted_string = selection_sort(user_input)

print("Original string:", user_input)
print("Sorted string (Selection Sort):", sorted_string)



# # -------------------------- Descending Order --------------------------
# def selection_sort(s):
#     arr = list(s)   # convert string to list of characters
#     n = len(arr)

#     for i in range(n - 1):
#         min_index = i
#         for j in range(i + 1, n):
#             if arr[j] > arr[min_index]:  # compare characters for descending   
#                 min_index = j
#         # Swap smallest character
#         arr[i], arr[min_index] = arr[min_index], arr[i]

#     return "".join(arr)   # convert back to string


# # ---- Main Program ----
# user_input = input("Enter a string: ")
# sorted_string = selection_sort(user_input)

# print("Original string:", user_input)
# print("Sorted string (Selection Sort):", sorted_string)
