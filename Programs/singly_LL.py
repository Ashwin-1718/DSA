# Define the Node class
class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Reference to the next node (initially None)

# Define the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize an empty list with no head

    # Method to insert a node at the beginning
    def insert_at_first(self, data):
        new_node = Node(data)  # Create a new node
        new_node.next = self.head  # Point the new node to the current head
        self.head = new_node  # Make the new node the new head
    
    # Method to insert a node at the end
    def insert_at_last(self, data):
        new_node = Node(data)  # Create a new node
        if not self.head:  # If the list is empty
            self.head = new_node  # The new node becomes the head
        else:
            current = self.head
            while current.next:  # Traverse to the last node
                current = current.next
            current.next = new_node  # Append the new node to the last node

    # Method to delete the first node
    def delete_first(self):
        if self.head:  # If the list is not empty
            self.head = self.head.next  # Make the second node the new head
        else:
            print("List is empty, no node to delete.")

    # Method to delete the last node
    def delete_last(self):
        if self.head:  # If the list is not empty
            if self.head.next is None:  # If there's only one node
                self.head = None  # Set the head to None, making the list empty
            else:
                current = self.head
                while current.next and current.next.next:  # Traverse to the second-last node
                    current = current.next
                current.next = None  # Remove the last node
        else:
            print("List is empty, no node to delete.")
    
    # Method to display the linked list
    def display(self):
        if not self.head:  # Check if the list is empty
            print("List is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Function to display the menu and perform operations
def menu():
    ll = LinkedList()  # Create an empty linked list
    while True:
        print("\n--- Linked List Menu ---")
        print("1. Insert at First")
        print("2. Insert at Last")
        print("3. Delete First Node")
        print("4. Delete Last Node")
        print("5. Display List")
        print("6. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            data = int(input("Enter data to insert at first: "))
            ll.insert_at_first(data)
        elif choice == 2:
            data = int(input("Enter data to insert at last: "))
            ll.insert_at_last(data)
        elif choice == 3:
            ll.delete_first()
        elif choice == 4:
            ll.delete_last()
        elif choice == 5:
            ll.display()
        elif choice == 6:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the program
menu()
