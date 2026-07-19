global top,max_elements,stack
stack=[]
top=0

def main():
    global max_elements
    max_elements=int(input("Enter maximum number of elements for the stack\n"))
    while(True):
        print("---------Menu----------")
        print("1) Push")
        print("2) Pop")
        print("3) Display")
        print("4) Exit")
        choice=int(input("Enter your choice (1-4)"))
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
                print("Enter choice value between 1-4")
def push():
    global top,max_elements,stack
    if top>=max_elements:
        print("Stack overflow")
    else:
        item=input("Enter item to be pushed")
        top=top+1
        stack.append(item)
        print("Item pushed successfully!!")
        display()
    
def pop():
    global top,max_elements,stack
    if top<=0:
        print("Stack underflow")
    else:
        item=stack.pop()
        top=top-1
        print("Item popped successfully!!",item)

def display():
    global top
    if(top==0):
        print("Stack is empty")
    else:
        print("Items in stack")
        for i in stack:
            print(i,end="\n")

main()