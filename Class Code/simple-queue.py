# Global variables
queue = []
front = -1
rear = -1
max_elements = 0

# Insert element in queue
def insert():
    global front, rear, queue, max_elements
    if rear >= (max_elements - 1):
        print("Overflow !!")
    else:
        item = input("Enter item: ")
        if front == -1:
            front = 0
        rear += 1
        if len(queue) <= rear:
            queue.append(item)  # add new item
        else:
            queue[rear] = item  # overwrite in case of reuse

# Delete element from queue
def delete():
    global front, rear, queue
    if front == -1 or front > rear:
        print("Underflow !!")
    else:
        print(queue[front], "deleted successfully !!")
        front += 1
        if front > rear:  # reset queue when empty
            front = rear = -1

# Display queue
def display():
    global front, rear, queue
    if front == -1 or front > rear:
        print("Queue is empty !!")
    else:
        print("Queue contents:")
        for i in range(front, rear + 1):
            print(queue[i])

# Main function with menu
def main():
    global max_elements
    max_elements = int(input("Enter size of the queue: "))
    while True:
        print('''
        ---- Menu ----
        1) Enqueue (Insert)
        2) Dequeue (Delete)
        3) Display
        4) Exit
        ''')
        choice = int(input("Enter your choice: "))
        
        match choice:
            case 1:
                insert()
            case 2:
                delete()
            case 3:
                display()
            case 4:
                print("Exiting...")
                break
            case _:
                print("Invalid choice!")

main()