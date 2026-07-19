class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at first
    def insert_first(self, data):
        new_node = Node(data)
        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node
        print("Inserted at first")

    # Insert at last
    def insert_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print("Inserted at last")
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp
        print("Inserted at last")

    # Delete first
    def delete_first(self):
        if self.head is None:
            print("List is empty")
            return

        print("Deleted:", self.head.data)
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    # Delete last
    def delete_last(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            print("Deleted:", self.head.data)
            self.head = None
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        print("Deleted:", temp.data)
        temp.prev.next = None

    # Display forward
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        print("List (Forward):", end=" ")
        while temp:
            print(temp.data, "<->", end=" ")
            temp = temp.next
        print("None")

    # Display reverse
    def display_reverse(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        print("List (Reverse):", end=" ")
        while temp:
            print(temp.data, "<->", end=" ")
            temp = temp.prev
        print("None")

    # Count nodes
    def count_nodes(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        print("Total nodes:", count)


# ---------------- Menu ----------------

dll = DoublyLinkedList()

while True:
    print("\n====== Doubly Linked List Menu ======")
    print("1) Insert at first")
    print("2) Insert at last")
    print("3) Delete first")
    print("4) Delete last")
    print("5) Display")
    print("6) Display in reverse")
    print("7) Count nodes")
    print("8) Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            dll.insert_first(input("Enter data: "))
        case 2:
            dll.insert_last(input("Enter data: "))
        case 3:
            dll.delete_first()
        case 4:
            dll.delete_last()
        case 5:
            dll.display()
        case 6:
            dll.display_reverse()
        case 7:
            dll.count_nodes()
        case 8:
            print("Exiting program...")
            break
        case _:
            print("Invalid choice")