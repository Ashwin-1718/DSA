class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def ins_first(self, data):
        new_node = Node(data)
        new_node.next = self.head 
        self.head = new_node
        print(f"Inserted {data} at the beginning.")

    def ins_last(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        print(f"Inserted {data} at the end.")

    def del_first(self):
        if not self.head:
            print("List is empty, nothing to delete.")
        else:
            print(f"Deleted: {self.head.data}")
            self.head = self.head.next

    def del_last(self):
        if not self.head:
            print("List is empty, nothing to delete.")
        elif not self.head.next: 
            print(f"Deleted: {self.head.data}")
            self.head = None
        else:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            print(f"Deleted: {temp.next.data}")
            temp.next = None

    def display(self):
        if not self.head:
            print("List is empty.")
        else:
            temp = self.head
            while temp:
                print(temp.data, "--->", end=" ")
                temp = temp.next
            print("None")


def main():
    ll = LinkedList()
    while True:
        print("\n====== Menu ======")
        print("1) Insert at first")
        print("2) Insert at last")
        print("3) Delete first")
        print("4) Delete last")
        print("5) Display")
        print("6) Exit")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                data = input("Enter data: ")
                ll.ins_first(data)
            case 2:
                data = input("Enter data: ")
                ll.ins_last(data)
            case 3:
                ll.del_first()
            case 4:
                ll.del_last()
            case 5:
                ll.display()
            case 6:
                print("Exiting program...")
                return
            case _:
                print("Invalid choice! Please enter between 1-6.")

main()