global front,rear,queue,max_elements
front=-1
rear=-1
queue=[]

def insert():
    global front,rear,queue
    if (rear + 1)%max_elements == front:
        print("Queue overflow!!")
    else:
        item=input("Enter the item: ")
        if front==-1:
            front=0
        rear=(rear + 1) % max_elements
        if len(queue)<=rear:
            queue.append(item)
        else:
            queue[rear]=item
        print(item, "inserted successfully!!")

def delete():
    global front,rear,queue
    if front==-1:
        print("Queue underflow!!")       
    else:
        item=queue[front]
        if front==rear:
            front=rear=-1
        else:
            front=(front + 1)%max_elements
        print(item,"deleted successfully!!")

def display():
    if front==-1:
        print("Queue is empty")
    else:
        print("Elements is queue:")
        if front<=rear:
            for i in range(front,rear + 1):
                print(queue[i])
        else:
            for i in range(front,max_elements):
                print(queue[i])
            for i in range(0,rear + 1):
                print(queue[i])


def main():
    global max_elements
    max_elements=int(input("Enter queue size: "))
    while(True):
        print("====Menu===")
        print("1) Insert")
        print("2) Delete")
        print("3) Display")
        print("4) Exit")
        choice=int(input("Enter your choice: "))
        match choice:
            case 1:
                insert()
            case 2:
                delete()
            case 3:
                display()
            case 4:
                return
            case _:
                print("Enter valid choice!!(1-4)")

main()