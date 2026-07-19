# #Stack Implementation in Python
# stack = []
# MAX_SIZE = input(int("Enter Stack Size: "))

# while True:
#     print("-----Menu-----")
#     print("1 for Push")
#     print("2 for pop")
#     print("3 for display")
#     print("4 for Exit")

#     choice = input("Enter your choice (1-4): ")

#     match choice:
#         case '1':
#             if len(stack) >= MAX_SIZE:
#                 print("Stack Overflow! Cannot push more elements.")
#             else:
#                 value = input("Enter value to push:")
#                 stack.append(value)
#                 print(f"{value} pushed into the stack.")

#         case '2':
#             if len(stack) == 0:
#                 print("Stack Underflow! Stack is empty.")
#             else:
#                 popped = stack.pop()
#                 print(f"Popped value: {popped}")

#         case '3':
#             if len(stack) == 0:
#                 print("Stack is empty.")
#             else:
#                 print("Stack elements (top to bottom):")
#                 for item in reversed(stack):
#                     print(item)

#         case '4':
#             print("Exiting program. Goodbye!")
#             break

#         case _:
#             print("Invalid input! Please enter a number between 1 and 4.")
                
            