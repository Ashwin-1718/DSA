class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    # Check if queue is empty
    def is_empty(self):
        return self.front == -1

    # Check if queue is full
    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    # Enqueue operation
    def enqueue(self, value):
        if self.is_full():
            print("Queue Overflow! Cannot insert.")
            return

        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = value
        print(value, "inserted.")

    # Dequeue operation
    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow! Nothing to delete.")
            return

        removed = self.queue[self.front]

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        print(removed, "deleted.")

    # Display queue
    def display(self):
        if self.is_empty():
            print("Queue is Empty.")
            return

        print("Circular Queue:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

    # Peek front element
    def peek_front(self):
        if self.is_empty():
            print("Queue is Empty.")
        else:
            print("Front element:", self.queue[self.front])

    # Peek rear element
    def peek_rear(self):
        if self.is_empty():
            print("Queue is Empty.")
        else:
            print("Rear element:", self.queue[self.rear])

    # Count total elements
    def count_elements(self):
        if self.is_empty():
            print("Total elements: 0")
        else:
            count = (self.rear - self.front + self.size) % self.size + 1
            print("Total elements:", count)

    # Search element
    def search(self, key):
        if self.is_empty():
            print("Queue is Empty.")
            return

        i = self.front
        pos = 0
        while True:
            if self.queue[i] == key:
                print(f"{key} found at position {pos}")
                return
            if i == self.rear:
                break
            i = (i + 1) % self.size
            pos += 1

        print(f"{key} not found in queue.")

    # Count occurrence of element
    def count_occurrence(self, key):
        if self.is_empty():
            print("Queue is Empty.")
            return

        count = 0
        i = self.front
        while True:
            if self.queue[i] == key:
                count += 1
            if i == self.rear:
                break
            i = (i + 1) % self.size

        print(f"{key} occurs {count} times.")


# ---------------- Menu Driven Program ----------------

size = int(input("Enter size of Circular Queue: "))
cq = CircularQueue(size)

while True:
    print("\n------ Circular Queue Menu ------")
    print("1. Enqueue (Insert)")
    print("2. Dequeue (Delete)")
    print("3. Display")
    print("4. Peek Front")
    print("5. Peek Rear")
    print("6. Count Elements")
    print("7. Search Element")
    print("8. Count Occurrence")
    print("9. Exit")
    

    choice = input("Enter your choice: ")

    if choice == "1":
        cq.enqueue(input("Enter value: "))

    elif choice == "2":
        cq.dequeue()

    elif choice == "3":
        cq.display()

    elif choice == "4":
        cq.peek_front()

    elif choice == "5":
        cq.peek_rear()

    elif choice == "6":
        cq.count_elements()

    elif choice == "7":
        cq.search(input("Enter element to search: "))

    elif choice == "8":
        cq.count_occurrence(input("Enter element: "))

    elif choice == "9":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please enter 1–9.")