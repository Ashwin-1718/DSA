class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CLL:
    def __init__(self):
        self.head = None

    # Insert at first
    def ins_first(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            self.head = new_node
        print("Node inserted successfully!!")

    # Insert at last
    def ins_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
        print("Node inserted successfully!!")

    # Delete first
    def del_first(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            print(self.head.data, "deleted successfully")
            self.head = None
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = self.head.next
        self.head = self.head.next
        print("Node deleted successfully")

    # Delete last
    def del_last(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            print(self.head.data, "deleted successfully")
            self.head = None
            return

        temp = self.head
        while temp.next.next != self.head:
            temp = temp.next

        print(temp.next.data, "deleted successfully")
        temp.next = self.head

    # Display
    def display(self):
        if self.head is None:
            print("List is empty!!")
            return

        temp = self.head
        while True:
            print(temp.data, end="-->")
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")

    # 🔥 Variation 1: Count nodes
    def count_nodes(self):
        if self.head is None:
            print("Total nodes: 0")
            return

        count = 1
        temp = self.head.next
        while temp != self.head:
            count += 1
            temp = temp.next
        print("Total nodes:", count)

    # 🔥 Variation 2: Search element
    def search(self, key):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        pos = 0
        while True:
            if temp.data == key:
                print(f"{key} found at position {pos}")
                return
            temp = temp.next
            pos += 1
            if temp == self.head:
                break

        print(f"{key} not found in the list")

    # 🔥 Variation 3: Count occurrence
    def count_occurrence(self, key):
        if self.head is None:
            print("List is empty")
            return

        count = 0
        temp = self.head
        while True:
            if temp.data == key:
                count += 1
            temp = temp.next
            if temp == self.head:
                break

        print(f"{key} occurs {count} times")

    # 🔥 Variation 4: Peek head
    def peek_head(self):
        if self.head is None:
            print("List is empty")
        else:
            print("Head element:", self.head.data)

    # 🔥 Variation 5: Check empty
    def is_empty(self):
        if self.head is None:
            print("List is empty")
        else:
            print("List is not empty")

def main():
    ll1 = CLL()

    while True:
        print("\n====== Circular Linked List Menu ======")
        print("1) Insert at first")
        print("2) Insert at last")
        print("3) Delete first")
        print("4) Delete last")
        print("5) Display")
        print("6) Count nodes")
        print("7) Search element")
        print("8) Count occurrence")
        print("9) Peek head")
        print("10) Check empty")
        print("11) Exit")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                ll1.ins_first(input("Enter data: "))
            case 2:
                ll1.ins_last(input("Enter data: "))
            case 3:
                ll1.del_first()
            case 4:
                ll1.del_last()
            case 5:
                ll1.display()
            case 6:
                ll1.count_nodes()
            case 7:
                ll1.search(input("Enter element to search: "))
            case 8:
                ll1.count_occurrence(input("Enter element: "))
            case 9:
                ll1.peek_head()
            case 10:
                ll1.is_empty()
            case 11:
                print("Exiting program...")
                break
            case _:
                print("Enter valid choice")


main()
