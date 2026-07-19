class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print("Inserted at first", data)

    def last(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        print("Inserted at the end", data)

    def pos(self, pos, data):
        if pos == 0:
            self.first(data)
            return
        new_node = Node(data)
        temp = self.head
        i = 0
        while temp and i < pos - 1:
            temp = temp.next
            i += 1
        if not temp:
            print("Invalid position")
            return
        new_node.next = temp.next
        temp.next = new_node
        print("Inserted at position:", pos, "data:", data)

    def del_first(self):
        if not self.head:
            print("List is empty")
        else:
            print("Deleted:", self.head.data)
            self.head = self.head.next

    def del_last(self):
        if not self.head:
            print("List is empty")
        elif not self.head.next:
            print("Deleted:", self.head.data)
            self.head = None
        else:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            print("Deleted:", temp.next.data)
            temp.next = None

    def display(self):
        if not self.head:
            print("List is empty.")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next
            print("None")

def main():
    list = linkedlist()

    while True:
        print("""
        ---- Menu ----
        1 Insert at first
        2 Insert at last
        3 Insert at specific position
        4 Delete First
        5 Delete Last
        6 Display
        7 Exit
        """)

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                data = input("Enter data: ")
                list.first(data)

            case 2:
                data = input("Enter data: ")
                list.last(data)

            case 3:
                pos = int(input("Enter position: "))
                data = input("Enter data: ")
                list.pos(pos, data)

            case 4:
                list.del_first()

            case 5:
                list.del_last()

            case 6:
                list.display()

            case 7:
                return

            case _:
                print('Enter Number between 1 to 7')
main()