stack = []
max_size = int(input("Enter Stack Size:- "))

def main():
    while True:
        print("-----Menu-----")
        print("1 For Push")
        print("2 For pop")
        print("3 For display")
        print("4 For Peek")
        print("5 For count")
        print("6 For Exit")

        choice = input("Enter your choice (1-6): ")
        
        match choice: 
            case '1':
                if len(stack) >= max_size:
                    print("Stack is OverFlow! Cannot Push More Element.")

                else:
                    value = input("Enter Value To Push. ")
                    stack.append(value)
                    print("value pushed into stack")

            case '2':
                if len(stack) == 0:
                    print("Stack is UnderFlow.")
                
                else:
                    items = stack.pop()
                    print(items, "poped")

            case '3':
                if len(stack) ==0:
                    print("stack is empty")
                else:
                    for item in stack:
                        print(item,end='\n')

            case '4':
                if len(stack) == 0:
                    print("Stack is empty. Cannot peek.")
                else:
                    print("Top element is:", stack[-1]) 

            case '5':
                print("Number of elements in stack:", len(stack))

            case '6':
                print("Exiting...")
                break

            case _:
                print("Invalid choice. Please enter a number between 1 and 6.")
main()