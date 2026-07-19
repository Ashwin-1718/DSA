class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CLL:
    def __init__(self):
        self.head = None

    def ins_first(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            new_node.next = self.head
            temp.next = new_node
            self.head = new_node
        print("Node inserted at first")

    def ins_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
        print("Node inserted at last")

    def del_first(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            print(self.head.data, "deleted")
            self.head = None
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        print(self.head.data, "deleted")
        temp.next = self.head.next
        self.head = self.head.next

    def del_last(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            print(self.head.data, "deleted")
            self.head = None
            return

        temp = self.head
        while temp.next.next != self.head:
            temp = temp.next

        print(temp.next.data, "deleted")
        temp.next = self.head

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")

    def search(self, key):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        pos = 0
        while True:
            if temp.data == key:
                print(key, "found at position", pos)
                return
            temp = temp.next
            pos += 1
            if temp == self.head:
                break

        print(key, "not found")

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

def main():
    cll = CLL()

    while True:
        print("-------CLL Menu-------")
        print("1 Insert at first")
        print("2 Insert at last")
        print("3 Delete first node")
        print("4 Delete last node")
        print("5 Display")
        print("6 Search")
        print("7 Count nodes")
        print("8 Exit")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                cll.ins_first(input("Enter data: "))
            case 2:
                cll.ins_last(input("Enter data: "))
            case 3:
                cll.del_first()
            case 4:
                cll.del_last()
            case 5:
                cll.display()
            case 6:
                cll.search(input("Enter element to search: "))
            case 7:
                cll.count_nodes()
            case 8:
                break
            case _:
                print("Enter valid choice")


main()