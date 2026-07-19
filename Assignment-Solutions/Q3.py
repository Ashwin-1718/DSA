class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    # Check full
    def isFull(self):
        return (self.rear + 1) % self.size == self.front

    # Check empty
    def isEmpty(self):
        return self.front == -1

    # Insert element
    def insert(self, value):
        if self.isFull():
            print("Queue is Full!")
            return
        if self.isEmpty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        print(value, "inserted.")

    # Delete element
    def delete(self):
        if self.isEmpty():
            print("Queue is Empty!")
            return
        data = self.queue[self.front]
        if self.front == self.rear:   # only one element left
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print(data, "deleted.")

    # Display elements
    def display(self):
        if self.isEmpty():
            print("Queue is Empty!")
            return
        print("Queue:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()


# ---------------- Menu ----------------
n = int(input("Enter size of Circular Queue: "))
cq = CircularQueue(n)

while True:
    print("\n1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        val = int(input("Enter value: "))
        cq.insert(val)
    elif ch == 2:
        cq.delete()
    elif ch == 3:
        cq.display()
    elif ch == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
