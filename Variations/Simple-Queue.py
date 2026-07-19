def main():
    queue = []
    max_size = int(input("Enter size of the queue: "))

    while True:
        print("""
        -------- Menu --------
        1) Enqueue (Insert)
        2) Dequeue (Delete)
        3) Display
        4) Search Element
        5) Count Elements
        6) Peek (Front Element)
        7) Remove Specific Element
        8) Find Max & Min
        9) Reverse Queue
        10) Exit
        -----------------------
        """)

        choice = input("Enter your choice: ")

        match choice:

            # 1. Enqueue
            case "1":
                if len(queue) >= max_size:
                    print("Queue Overflow")
                else:
                    item = input("Enter item: ")
                    queue.append(item)
                    print("Inserted:", item)

            # 2. Dequeue
            case "2":
                if len(queue) == 0:
                    print("Queue Underflow")
                else:
                    removed = queue.pop(0)
                    print("Deleted:", removed)

            # 3. Display
            case "3":
                if len(queue) == 0:
                    print("Queue is empty")
                else:
                    print("Queue contents:", queue)

            # 4. Search Element
            case "4":
                if not queue:
                    print("Queue is empty")
                else:
                    element = input("Enter element to search: ")
                    if element in queue:
                        pos = queue.index(element)
                        print(f"Element '{element}' found at position {pos}")
                    else:
                        print("Element not found in queue")

            # 5. Count Elements
            case "5":
                print("Total elements in queue:", len(queue))

            # 6. Peek Front Element
            case "6":
                if not queue:
                    print("Queue is empty")
                else:
                    print("Front element:", queue[0])

            # 7. Remove Specific Element
            case "7":
                if not queue:
                    print("Queue is empty")
                else:
                    target = input("Enter element to remove: ")
                    if target in queue:
                        queue.remove(target)
                        print("Removed:", target)
                    else:
                        print("Element not found")

            # 8. Find Max & Min
            case "8":
                if not queue:
                    print("Queue is empty")
                else:
                    try:
                        print("Max element:", max(queue))
                        print("Min element:", min(queue))
                    except TypeError:
                        print("Cannot find max/min for mixed data types")

            # 9. Reverse Queue
            case "9":
                if not queue:
                    print("Queue is empty")
                else:
                    queue.reverse()
                    print("Queue reversed:", queue)

            # 10. Exit Program
            case "10":
                print("Exiting...")
                break

            # Invalid choice
            case _:
                print("Invalid choice! Enter a number between 1–10.")

main()