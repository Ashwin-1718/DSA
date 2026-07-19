# Class Code
global max_elements,top,stack
top = 0
stack = []

def push():
    global top, stack
    if top >= max_elements:
        print("overflow")
    else:
        item = input("Enter the item")
        stack.append(item)
        top = top +1
        print(item," pushed successfully")
        
def pop():
    global top, max_elements
    if(top <= 0):
        print("underflow")
    else:
        item = stack.pop()
        top =top -1
        print(item," pop ho gya bc")

def display():
    if top == 0:
        print("stack is empty")
    else:
        for item in stack:
            print(item, end=" ")

def main():
    global max_elements
    max_elements = int(input("ENter stack size: "))
    while(True):
        print('----menu-----')
        print('1. Add item to stack ')
        print('2. Remove the item from stack')
        print('3. Display Stack')
        print('4. Exit')
        choice = int(input("enter choice: "))
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
                print("invalid choice")
                
main()