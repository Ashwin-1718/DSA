global max_elements,top,stack
stack=[]
top=0

def push():
    global top,stack
    if top>=max_elements:
        print("Overflow")
    else:
        item=input(f"Enter item:\t")
        top=top+1
        stack.append(item)
        print("Inserted successfully!!")

def pop():
    global top,stack
    if top<=0:
        print("Underflow!!")
    else:
        item=stack.pop()
        print(item," popped!!")
        top=top-1

def display():
    if top==0:
        print("Stack is empty")
    else:
        for item in stack:
            print(item,end="\n")

def main():
    global max_elements
    max_elements=int(input(f"Enter stack size:\t"))
    while(True):
        print("------Menu-----")
        print("1) PUSH")
        print("2) POP")
        print("3) Display")
        print("4) Exit")
        choice=int(input(f"Enter choice:\t"))
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
                print("Enter choice between (1-4)")
        
main()