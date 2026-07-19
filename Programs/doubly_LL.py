class Node:
    def __init__(self, data):
        self.data = data  # Data of the node
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initially, the list is empty

    # Method to insert a node at the end of the list
    def ins_last(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty, make the new node the head
            self.head = new_node
            return
        temp = self.head
        while temp.next:  # Traverse to the last node
            temp = temp.next
        temp.next = new_node  # Link the new node to the last node
        new_node.prev = temp  # Link the last node to the new node

    # Method to insert a node at the beginning of the list
    def ins_first(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        new_node.next = self.head  # Link the new node to the head
        self.head.prev = new_node  # Link the head to the new node
        self.head = new_node  # Make the new node the head

    # Method to delete a node from the front
    def delete_first(self):
        if not self.head:  # If the list is empty
            print("List is empty.")
            return
        if self.head.next:  # If there's more than one node
            self.head = self.head.next
            self.head.prev = None
        else:  # If there's only one node
            self.head = None

    # Method to delete a node from the end
    def delete_last(self):
        if not self.head:  # If the list is empty
            print("List is empty.")
            return
        if not self.head.next:  # If there's only one node
            self.head = None
            return
        temp = self.head
        while temp.next:  # Traverse to the last node
            temp = temp.next
        temp.prev.next = None  # Remove the link to the last node

    # Method to display the list from head to tail
    def display(self):
        current = self.head
        if not current:  # If the list is empty
            print("List is empty.")
            return
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    # Method to display the list from tail to head
    def display_reverse(self):
        current = self.head
        if not current:  # If the list is empty
            print("List is empty.")
            return
        while current.next:  # Traverse to the last node
            current = current.next
        # Traverse backward from the last node
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")


# Main function to implement the menu
def menu():
    dll = DoublyLinkedList()
    while True:
        print("\nDoubly Linked List Menu")
        print("1. Insert at First")
        print("2. Insert at Last")
        print("3. Delete from First")
        print("4. Delete from Last")
        print("5. Display List")
        print("6. Display List in Reverse")
        print("7. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            data = int(input("Enter data to insert at first: "))
            dll.ins_first(data)
        elif choice == 2:
            data = int(input("Enter data to insert at last: "))
            dll.ins_last(data)
        elif choice == 3:
            dll.delete_first()
        elif choice == 4:
            dll.delete_last()
        elif choice == 5:
            dll.display()
        elif choice == 6:
            dll.display_reverse()
        elif choice == 7:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 7.")

# Run the menu function
menu()
