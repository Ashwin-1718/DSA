def main():
    queue = []
    max_size = int(input("Enter size of the queue: "))

    while True:
        print("""
        ---- Menu ----
        1) Enqueue (Insert)
        2) Dequeue (Delete)
        3) Display
        4) Exit
        """)
        
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                if len(queue) >= max_size:
                    print("Queue Overflow ")
                else:
                    item = input("Enter item: ")
                    queue.append(item)
                    print("Inserted:", item)

            case "2":
                if len(queue) == 0:
                    print("Queue Underflow")
                else:
                    removed = queue.pop(0)
                    print("Deleted:", removed) 

            case "3":
                if len(queue) == 0:
                    print("Queue is empty")
                else:
                   print("Queue contents:", queue)
                   
            case "4":
                print("Exiting...")
                break   

            case _:
                print("Please enter number between 1 to 4")        
main()