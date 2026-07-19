class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Insert at first
    def ins_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} at the beginning.")

    # 2. Insert at last
    def ins_last(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        # print(f"Inserted {data} at the end.")
        print("Inserted at the end.", data)

    # 3. Delete first
    def del_first(self):
        if not self.head:
            print("List is empty, nothing to delete.")
        else:
            # print(f"Deleted: {self.head.data}")
            print("Deleted:", self.head.data)
            self.head = self.head.next

    # 4. Delete last
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

    # 5. Display
    def display(self):
        if not self.head:
            print("List is empty.")
        else:
            temp = self.head
            while temp:
                print(temp.data, "--->", end=" ")
                temp = temp.next
            print("None")

    # 6. Search element
    # def search(self, key):
    #     temp = self.head
    #     pos = 0
    #     while temp:
    #         if temp.data == key:
    #             print(f"{key} found at position {pos}")
    #             return
    #         temp = temp.next
    #         pos += 1
    #     print(f"{key} not found in the list.")

    def search(self, ele):
        temp = self.head
        pos = 0
        while temp:
            if temp.data == ele:
                # print(f"{key} found at position {pos}")
                print(ele, "found at position", pos)
                return
            temp = temp.next
            pos += 1
        # print(f"{key} not found in the list.")
        print("Element not found", ele)

    # 7. Count nodes
    def count_nodes(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        print("Total nodes:", count)

    # 8. Insert at specific position
    def insert_pos(self, pos, data):
        if pos == 0:
            self.ins_first(data)
            return

        new_node = Node(data)
        temp = self.head
        i = 0

        while temp and i < pos - 1:
            temp = temp.next
            i += 1

        if not temp:
            print("Invalid position!")
            return

        new_node.next = temp.next
        temp.next = new_node
        print(f"{data} inserted at position {pos}")

    # 9. Delete from specific position
    def delete_pos(self, pos):
        if self.head is None:
            print("List is empty.")
            return

        if pos == 0:
            self.del_first()
            return

        temp = self.head
        i = 0

        while temp.next and i < pos - 1:
            temp = temp.next
            i += 1

        if not temp.next:
            print("Invalid position!")
            return

        print(f"Deleted: {temp.next.data}")
        temp.next = temp.next.next

    # 10. Reverse linked list
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev
        print("Linked list reversed.")

    # 11. Find minimum and maximum
    def find_min_max(self):
        if not self.head:
            print("List is empty.")
            return

        temp = self.head
        minimum = maximum = temp.data

        while temp:
            if temp.data < minimum:
                minimum = temp.data
            if temp.data > maximum:
                maximum = temp.data
            temp = temp.next

        print("Min:", minimum)
        print("Max:", maximum)

    # 12. Delete specific value
    def delete_value(self, key):
        if not self.head:
            print("List is empty.")
            return

        if self.head.data == key:
            print(f"Deleted: {key}")
            self.head = self.head.next
            return

        temp = self.head
        while temp.next and temp.next.data != key:
            temp = temp.next

        if not temp.next:
            print("Value not found.")
            return

        print(f"Deleted: {temp.next.data}")
        temp.next = temp.next.next


# ========================== Menu Program ==========================

def main():
    ll = LinkedList()

    while True:
        print("\n====== Menu ======")
        print("1) Insert at first")
        print("2) Insert at last")
        print("3) Delete first")
        print("4) Delete last")
        print("5) Display")
        print("6) Search element")
        print("7) Count nodes")
        print("8) Insert at specific position")
        print("9) Delete at specific position")
        print("10) Reverse linked list")
        print("11) Find Min & Max")
        print("12) Delete specific value")
        print("13) Exit")

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
                key = input("Enter value to search: ")
                ll.search(key)

            case 7:
                ll.count_nodes()

            case 8:
                pos = int(input("Enter position: "))
                data = input("Enter data: ")
                ll.insert_pos(pos, data)

            case 9:
                pos = int(input("Enter position: "))
                ll.delete_pos(pos)

            case 10:
                ll.reverse()

            case 11:
                ll.find_min_max()

            case 12:
                key = input("Enter value to delete: ")
                ll.delete_value(key)

            case 13:
                print("Exiting program...")
                return

            case _:
                print("Invalid choice! Enter between 1–13.")

main()