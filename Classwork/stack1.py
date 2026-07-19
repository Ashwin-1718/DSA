global top,max_elements,stack
top=0
stack=[]

def push():
    global top,stack
    if top>=max_elements:
        print("Overflow!!")
    else:
        item=input("Enter item: ")
        top=top+1
        stack.append(item)
        print(item," pushed successfully!!")

def pop():
    global top,stack
    if top<=0:
        print("Underflow!!")
    else:
        item=stack.pop()
        top=top-1
        print(item," popped!!")

def display():
    if top==0:
        print("Stack is empty")
    else:
        for item in stack:
            print(item,end="\n")

def main():
    global max_elements
    max_elements=int(input("Enter the sizen of the stack: "))
    while(True):
        print("-----Menu-----")
        print("1) PUSH")
        print("2) POP")
        print("3) Display")
        print("4) Exit")
        choice=int(input("Enter choice: "))
        match choice:
            case 1:
                push()
            case 2:
                pop()
            case 3:
                display()
            case 4:
                return
            case _:
                print("Invalid choice!!")

main()