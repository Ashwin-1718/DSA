class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    # Check if the queue is empty
    def is_empty(self):
        return self.front == -1

    # Check if the queue is full
    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    # Insert element into circular queue
    def enqueue(self, value):
        if self.is_full():
            print("Queue Overflow! Cannot insert.")
            return

        # First element insertion
        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = value
        print(value, "inserted.")

    # Delete element from circular queue
    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow! Nothing to delete.")
            return

        removed = self.queue[self.front]

        # If only one element was present
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        print(removed, "deleted.")

    # Display the queue contents
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


# ---------------- Menu Driven Program ----------------

size = int(input("Enter size of Circular Queue: "))
cq = CircularQueue(size)

while True:
    print("\n1. Enqueue (Insert)")
    print("2. Dequeue (Delete)")
    print("3. Display")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        value = input("Enter value: ")
        cq.enqueue(value)

    elif choice == "2":
        cq.dequeue()

    elif choice == "3":
        cq.display()

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please enter 1–4.")
        