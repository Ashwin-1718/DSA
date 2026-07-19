global front,rear,max_elements,queue
queue=[]
front=-1
rear=-1

def insert():
    global rear,front,queue
    if rear>=(max_elements - 1):
        print("Overflow!!")
    else:
        if front==-1:
            front=0
        item=input("Enter item: ")
        rear = rear + 1
        queue.append(item)
        print(item, "inserted successfully")

def delete():
    global rear,front,queue
    if front<0:
        print("Underflow!!")
    else:
        item=queue[front]
        print(item, "deleted successfully")
        if front==rear:
            front=rear=-1
        else:
            front = front + 1

def display():
    if front<0:
        print("Queue is empty!!")
    else:
        for i in range(front,rear+1):
            print(queue[i])

def main():
    global max_elements
    max_elements=int(input("Enter queue size: "))
    while(True):
        print("-----Menu----")
        print("1) Enqeue(Insert)")
        print("2) Deqeue(Delete)")
        print("3) Display")
        print("4) Exit")
        choice=int(input("Enter choice (1-4): "))
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
                print("Enter valid choice (1-4)")


main()