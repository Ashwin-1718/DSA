class Node:
    def __init__(self,item):
        self.data=item
        self.next=None

class CircularLL:
    def __init__(self):
        self.head=None

    def ins_first(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            self.head.next=self.head
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=new_node
            new_node.next=self.head
            head=new_node

    def ins_last(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            self.head.next=self.head
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=new_node
            new_node.next=self.head


    def display(self):
        if not self.head:
            print("List is empty")
        else:
            temp=self.head
            while True:
                print(temp.data,"--->",end="\t")
                temp=temp.next
                if (temp == self.head):
                    break
            print("(head)")
def main():
    cll1=CircularLL()
    while True:
        print("======Menu======")
        print("1) Insert at first")
        print("2) Insert at last")
        print("3) Delete first")
        print("4) Delete last")
        print("5) Display")
        print("6) Exit")
        
        choice=int(input(f'Enter your choice:\t'))

        match choice:
            case 1:
                data=input(f'Enter data:\t')
                cll1.ins_first(data)
            case 2:
                data=input(f'Enter data:\t')
                cll1.ins_last(data)
            # case 3:
            #     ll1.del_first()
            # case 4:
            #     ll1.del_last()
            case 5:
                cll1.display()
            case 6:
                return
            case _:
                print("Enter valid choice")
            
main()