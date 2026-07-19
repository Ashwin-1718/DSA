stack = []
max_size = int(input("Enter Stack Size:- "))

def main():
    while True:
        print("-----Menu-----")
        print("1 For Push")
        print("2 For pop")
        print("3 For display")
        print("4 For Exit")

        choice = input("Enter your choice (1-4): ")
        
        match choice:
            case '1':
                if len(stack) >= max_size:
                    print("Stack is OverFlow! Cannot Puch More Element.")

                else:
                    value = input("Enter Value To Puch. ")
                    stack.append(value)
                    print("value puched into stack")

            case '2':
                if len(stack) == 0:
                    print("Stack is UnderFlow!.")

                else:
                    items = stack.pop()
                    print(items, "poped!")

            case '3':
                if len(stack) ==0:
                    print("stack is empty")
                else:
                    for item in stack:
                        print(item,end='\n')

            case '4':
                print("Exiting the program Good Bye!!.")
                break

            case _:
                print("Invalid choice. Please enter a number between 1 and 4.")
main()
