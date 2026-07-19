global max_elements, top, stack
top = 0
stack = []

def push():
    global top, stack
    if top >= max_elements:
        print("overflow")
    else:
        item = input("Enter the item: ")
        stack.append(item)
        top = top + 1
        print(item, "pushed successfully")

def pop():
    global top
    if top <= 0:
        print("underflow")
    else:
        item = stack.pop()
        top = top - 1
        print(item, "pop")

def display(): 
    if top == 0:
        print("stack is empty")
    else:
        print("Stack elements:", end=" ")
        for item in stack:
            print(item, end=" ")
        print()

def peek():
    if top == 0:
        print("stack is empty")
    else:
        print("Top element is:", stack[-1])

def count():
    print("Number of elements in stack:", top)

def main():
    global max_elements
    max_elements = int(input("Enter stack size: "))
    while True:
        print('----menu-----')
        print('1. Add item to stack')
        print('2. Remove the item from stack')
        print('3. Display')
        print('4. Peek')
        print('5. Count')
        print('6. Exit')
        choice = int(input("Enter choice: "))
        match choice:
            case 1:
                push()
            case 2:
                pop()
            case 3:
                display()
            case 4:
                peek()
            case 5:
                count()
            case 6:
                return
            case _:
                print("invalid choice")

main()