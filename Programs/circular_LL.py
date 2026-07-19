class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_first(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            self.head = new_node

    # Insert at the end
    def insert_last(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    # Delete the first node
    def delete_first(self):
        if not self.head:
            print("List is empty!")
            return
        elif self.head.next == self.head:  # Only one node in the list
            self.head = None
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            self.head = self.head.next
            current.next = self.head

    # Delete the last node
    def delete_last(self):
        if not self.head:
            print("List is empty!")
            return
        elif self.head.next == self.head:  # Only one node in the list
            self.head = None
        else:
            current = self.head
            while current.next.next != self.head:
                # prev = current
                current = current.next
            current.next = self.head

    # Display the list
    def display(self):
        if not self.head:
            print("List is empty!")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(head)")

# Main function to drive the program
def main():
    cll = CircularLinkedList()
    while True:
        print("\nMenu Options:")
        print("1. Insert First")
        print("2. Insert Last")
        print("3. Delete First")
        print("4. Delete Last")
        print("5. Display List")
        print("6. Exit")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            data = int(input("Enter the data to insert at first: "))
            cll.insert_first(data)
        elif choice == 2:
            data = int(input("Enter the data to insert at last: "))
            cll.insert_last(data)
        elif choice == 3:
            cll.delete_first()
        elif choice == 4:
            cll.delete_last()
        elif choice == 5:
            cll.display()
        elif choice == 6:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
