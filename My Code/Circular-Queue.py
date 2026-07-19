class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def isFull(self):
        return (self.rear + 1) % self.size == self.front

    def isEmpty(self):
        return self.front == -1

    def insert(self, data):
        if self.isFull():
            print("Queue is Full!")
            return
        if self.isEmpty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data
        print(f"{data} inserted")

    def delete(self):
        if self.isEmpty():
            print("Queue is Empty!")
            return
        removed = self.queue[self.front]
        if self.front == self.rear:  # only one element left
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print(f"Deleted: {removed}")

    def display(self):
        if self.isEmpty():
            print("Queue is Empty!")
            return
        print("Queue elements:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()


# ---------------- Menu-Driven Part ----------------
size = int(input("Enter the size of the Circular Queue: "))
cq = CircularQueue(size)

while True:
    print("\n====== Circular Queue Menu ======")
    print("1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        element = int(input("Enter element to insert: "))
        cq.insert(element)
    elif choice == 2:
        cq.delete()
    elif choice == 3:
        cq.display()
    elif choice == 4:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")