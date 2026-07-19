class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    # Check empty
    def is_empty(self):
        return self.front == -1

    # Check full
    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    # Insert (Enqueue)
    def enqueue(self, value):
        if self.is_full():
            print("Queue Overflow")
            return

        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = value
        print("Inserted:", value)

    # Delete (Dequeue)
    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return

        removed = self.queue[self.front]

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        print("Deleted:", removed)

    # Display
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return

        print("Circular Queue:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

    # Count total elements
    def count_elements(self):
        if self.is_empty():
            print("Total elements: 0")
        else:
            count = (self.rear - self.front + self.size) % self.size + 1
            print("Total elements:", count)

    # Count occurrence of an element
    def count_occurrence(self, key):
        if self.is_empty():
            print("Queue is empty")
            return

        count = 0
        i = self.front
        while True:
            if self.queue[i] == key:
                count += 1
            if i == self.rear:
                break
            i = (i + 1) % self.size

        print(key, "occurs", count, "times")


# ---------------- Menu Driven Program ----------------

size = int(input("Enter size of Circular Queue: "))
cq = CircularQueue(size)

while True:
    print("\n====== Circular Queue Menu ======")
    print("1) Insert")
    print("2) Delete")
    print("3) Display")
    print("4) Count total elements")
    print("5) Count occurrence of element")
    print("6) Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        cq.enqueue(input("Enter value: "))

    elif choice == "2":
        cq.dequeue()

    elif choice == "3":
        cq.display()

    elif choice == "4":
        cq.count_elements()

    elif choice == "5":
        cq.count_occurrence(input("Enter element: "))

    elif choice == "6":
        break

    else:
        print("Enter valid choice (1-6)")
