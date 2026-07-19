global front, rear, max_elements, queue

queue = []
front = -1
rear = -1

def main():
    global max_elements
    max_elements = int(input("Enter maximum number of elements for the queue\n"))
    
    while(True):
        print("---------Menu----------")
        print("1) Insert")
        print("2) Delete")
        print("3) Display")
        print("4) Exit")
        choice = int(input("Enter your choice (1-4)\t"))
        
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
                print("Enter choice value between 1-4")

def insert():
    global front, rear, max_elements, queue
    
    if (rear + 1) % max_elements == front:  # Check for queue overflow
        print("Queue overflow")
    else:
        item = input("Enter item to be inserted\t")
        if front == -1:  # The queue is initially empty
            front = 0
        rear = (rear + 1) % max_elements  # Circular increment of rear
        if len(queue) <= rear:
            queue.append(item)  # Extend the list if necessary
        else:
            queue[rear] = item  # Replace the item at the rear position
        print("Item inserted successfully!")
    print("Value of Rear:", rear, " Front:", front)

def delete():
    global front, rear, max_elements, queue
    
    if front == -1:  # Check for queue underflow
        print("Queue underflow")
    else:
        item = queue[front]
        print(item, "deleted successfully")
        
        if front == rear:  # Queue is now empty
            front = -1
            rear = -1
        else:
            front = (front + 1) % max_elements  
    print("Value of Rear:", rear, " Front:", front)

def display():
    global front, rear, max_elements, queue
    
    if front == -1: 
        print("Queue is empty")
    else:
        print("Items in queue:")
        if front <= rear:
            for i in range(front, rear + 1):
                print(queue[i], end="\n")
        else:  
            for i in range(front, max_elements):
                print(queue[i], end="\n")
            for i in range(0, rear + 1):
                print(queue[i], end="\n")

main()