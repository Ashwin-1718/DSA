def main():
    queue = []
    max_size = int(input("Enter size of the queue: "))

    while True:
        print("""
        ---- Menu ----
        1 Insert
        2 Delete
        3 Display
        4 Number Of Occurrences
        5 Exit
        """)
        
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                if len(queue) >= max_size:
                    print("Queue Overflow ")
                else:
                    Data = input("Enter Data: ")
                    queue.append(Data)
                    print("Inserted:", Data)

            case "2":
                if len(queue) == 0:
                    print("Queue Underflow")
                else:
                    remove = queue.pop(0)
                    print("Deleted:", remove) 

            case "3":
                if len(queue) == 0:
                    print("Queue is empty")
                else:
                   print(queue)

            case "4":
                if len(queue) == 0:
                    print("Queue is empty")
                else:
                    ele = input("Enter element: ")
                    count = queue.count(ele)
                    print("Element", ele, "occurs", count, "time")
                   
            case "5":
                break   

            case _:
                print("Please enter number between 1 to 5")        
main()